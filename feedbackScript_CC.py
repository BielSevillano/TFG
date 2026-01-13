import argparse
from google import genai
import jutge_api_client as jutge
import os
import time
import io
import subprocess
import sys
import re
from base64 import b64decode
import random
import numpy as np

translate_results = {
    "AC": "Accepted",
    "PE": "Presentation Error",
    "WA": "Wrong Answer",
    "IC": "Invalid Character",
    "EE": "Execution Error",
    "UE": "User Error",
    "CE": "Compilation Error",
    "NC": "Noncompliant Solution",
    "Pending": "Pending Submission",
    "SE": "Setter Error",
    "SC": "Scored",
    "IE": "Internal Error",
    "FE": "Fatal Errors"
}

def maintainability_parsing(output):
    match = re.search(r"(\d+\.\d+)", output)
    if match:
        return float(match.group(1))
    return None

def complexity_parsing(output):
    mapping = {"A": 100, "B": 85, "C": 70, "D": 55, "E": 40, "F": 25}
    grades = re.findall(r"\s([A-F])\s", output)
    if not grades:
        return 100
    scores = [mapping[g] for g in grades]
    return sum(scores) / len(scores)

def pylint_parsing(output):
    match = re.search(r"rated at (-?\d+\.\d+)/10", output)
    if match:
        return float(match.group(1)) * 10
    return None

def decode_solution(problem_id,file_path, number):
    with open(file_path, "r") as f:
        lines = f.readlines()
        i = 0
        while (lines[i].split()[0] != problem_id):
            i += 1
        k = 0
        while (k < number):
            if lines[i + k + 1].strip() and (lines[i + k + 1].split()[1] == "G++" or lines[i + k + 1].split()[1] == "P1++" 
                                             or lines[i + k + 1].split()[1] == "G++11"):
                k += 1
            else:
                i += 1
        line = lines[i + k].strip()
        base64_code = line.split()[-1]

        # Get the result and translate it
        result = line.split()[2]
        result = translate_results.get(result, result)
        try:
            decoded_bytes = b64decode(base64_code)
            decoded_text = decoded_bytes.decode("utf-8", errors="replace")
            return decoded_text, result

        except Exception as e:
            print(f"[ERROR] en línea {number}: {e}")

def prompt_solutions(dendrogram_file, program_number, prompt_length):
    dendro_data = np.load(dendrogram_file, allow_pickle=True).item()
    lnks = dendro_data["linkage"]
    programs = dendro_data["programs"]

    N = len(programs)

    most_distant_programs = set()

    for row in lnks[lnks[:,2].argsort()[::-1]]:
        id1, id2 = int(row[0]), int(row[1])
        if id1 < N:
            most_distant_programs.add(id1)
        if id2 < N:
            most_distant_programs.add(id2)
        if len(most_distant_programs) >= prompt_length:
            break

    most_distant_programs = list(most_distant_programs)
    for p in [programs[i] for i in most_distant_programs]:
        print(p)
    return [programs[i] for i in most_distant_programs if i != program_number][:prompt_length]

def get_key(current_key_index):
    with open("API_KEYS.txt", "r") as f:
        keys = f.readlines()
    return keys[current_key_index].strip()

def ask_for_feedback(client, model, prompt):
        intento = 0
        current_key_index = 0
        while (True):
            try:
                response = client.models.generate_content(model=model, contents=[prompt])
                return response.text
            
            except Exception as e:
                match = re.search(r"Please retry in (\d+)", str(e))
                if match:
                    if current_key_index >= 9:
                        current_key_index = 0
                        wait_time = int(match.group(1))
                        print(f"Esperando {wait_time} segundos antes de reintentar...")
                        time.sleep(wait_time)
                    else:
                        current_key_index += 1
                        client = genai.Client(api_key=get_key(current_key_index))
                        print(f"Key Switched: {get_key(current_key_index)}")
                    continue
                print(f"[WARNING] Intento {intento + 1} fallido: {e}")
                time.sleep((2 ** intento) + random.random())
                if intento >= 10:
                    intento += 1

DENDROGRAM_FILE = "./DENDROGRAMA_CC/DENDROGRAMAS/dendrogram_data.npy"

def main(email: str, password: str, tries: int, max_reviews: int):

    #take the problems ids from a text file
    problems_id = []
    with open("problems.txt", "r") as f:
        for line in f:
            problems_id.append(line.strip())
        f.close()

    # Initialize the GenAI client
    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
    prompt_length = 50
    number = random.randint(prompt_length, 120)
    compiler_id = "C++"
    model = "gemini-2.5-flash-lite"

    '''
    # Login to Jutge
    j = jutge.JutgeApiClient()
    j.login(email, password)
    '''
    path_solutions = "./DENDROGRAMA_CC/solucions.txt"
    path_solutions_relative = "solucions.txt"

    for problem_id in problems_id:
        if problem_id == "CHANGE":
            path_solutions = "./DENDROGRAMA_CC/solucionsPRO1.txt"
            path_solutions_relative = "solucionsPRO1.txt"
            continue
        solutions = []

        print(f"Generating dendrogram for problem {problem_id}...")
        cwd_original = os.getcwd()
        proc = subprocess.Popen(['python3', "./dendrogram.py", problem_id, str(max_reviews), path_solutions_relative], cwd="./DENDROGRAMA_CC")
        proc.wait()
        os.chdir(cwd_original)

        r = 1
        if (problem_id == "P31170_en"):
            r = 81
        while r <= max_reviews:

            solutions = prompt_solutions("./DENDROGRAMA_CC/DENDROGRAMAS/dendrogram_" + problem_id + ".npy", number, r)

            for i in range(tries):
                if (problem_id == "P31170_en" and r == 81 and i <= 3):
                    continue
                intento = 0
                while True:
                    try:
                        with open(f"./enunciados/{problem_id}.txt", "r") as f:
                            statement = f.read()
                            f.close()
                        break

                    except Exception as e:
                        print(f"[ERROR] No se pudo obtener el enunciado del problema {problem_id}: {e}")
                        time.sleep((2 ** intento) + random.random())
                        if intento >= 10:
                            intento += 1
                number = random.randint(prompt_length, 120)
                program, result = decode_solution(problem_id, path_solutions, number)

                prompt = f"""
                Write a feedback text for the following program that solves the problem described below.
                {statement}

                This is the program:

                {program}

                The result of the program is: {result}

                The feedback should include:
                - A brief summary of the problem and the solution approach.
                - An analysis of the code's strengths and weaknesses.
                - Suggestions for improvement, if any.

                You can rely on the following other possible solutions to the same problem for reference:
                {chr(10).join(solutions)}
                """
                answer = None
                while answer is None:
                    answer = ask_for_feedback(client, model, prompt)

                # Make a file for the prompt
                if not os.path.exists(f"./FEEDBACKS_CC/{problem_id}/Prompt_{r}_solutions/"):
                    os.makedirs(f"./FEEDBACKS_CC/{problem_id}/Prompt_{r}_solutions/", exist_ok=True)
                with open(f"./FEEDBACKS_CC/{problem_id}/Prompt_{r}_solutions/{i}_prompt.txt", "w") as f:
                    f.write(prompt)
                    print(f"Prompt saved to ./FEEDBACKS_CC/{problem_id}/Prompt_{r}_solutions/{i}_prompt.txt")
                    f.close()

                # Make a temp file with the feedback or create de directory if it doesn't exist
                if not os.path.exists(f"./FEEDBACKS_CC/{problem_id}/Prompt_{r}_solutions/"):
                    os.makedirs(f"./FEEDBACKS_CC/{problem_id}/Prompt_{r}_solutions/", exist_ok=True)
                with open(f"./FEEDBACKS_CC/{problem_id}/Prompt_{r}_solutions/{i}.md", "w") as f:
                    f.write(answer)
                    print(f"Program saved to ./FEEDBACKS_CC/{problem_id}/Prompt_{r}_solutions/{i}.md")
                    f.close()
            r += 10
    j.logout()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Script para generar feedback de soluciones.")
    parser.add_argument("email", help="Email de Jutge")
    parser.add_argument("password", help="Contraseña de Jutge")
    parser.add_argument("tries", type=int, help="Número de intentos por problema")
    parser.add_argument("max_reviews", type=int, help="Número máximo de soluciones por problema")
    args = parser.parse_args()
    main(args.email, args.password, args.tries, args.max_reviews)