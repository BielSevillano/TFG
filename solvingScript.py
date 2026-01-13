import argparse
from random import random
from google import genai
import jutge_api_client as jutge
import os
import time
import io
import subprocess
import sys
import re

def run_command(cmd):
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.stdout.strip() + result.stderr.strip()


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

def analyze(file_path):
    mi_output = run_command([sys.executable, "-m", "radon", "mi", "-s", file_path])
    mi_score = maintainability_parsing(mi_output)

    cc_output = run_command([sys.executable, "-m", "radon", "cc", file_path, "-s"])
    cc_score = complexity_parsing(cc_output)

    pylint_output = run_command([sys.executable, "-m", "pylint", file_path])
    pylint_score = pylint_parsing(pylint_output)

    if mi_score is None or cc_score is None or pylint_score is None:
        return 0
    
    return (mi_score + cc_score + pylint_score) / 3

def get_key(current_key_index):
    with open("API_KEYS.txt", "r") as f:
        keys = f.readlines()
    return keys[current_key_index].strip()

def ask_for_solution(client, model, prompt):
        intento = 0
        current_key_index = 0
        TIMERATE = 0
        if os.path.exists("time_log_solving.txt"):
            with open("time_log_solving.txt", "r") as f:
                times = f.readlines()
                if len(times) > 0:
                    TIMERATE = sum([float(t.strip()) for t in times]) / len(times)
        while (True):
            try:
                t = time.perf_counter()
                response = client.models.generate_content(model=model, contents=[prompt])
                t = t - time.perf_counter()
                if TIMERATE == 0:
                    TIMERATE = t
                else:
                    TIMERATE = (TIMERATE + t) / 2
                with open("time_log_solving.txt", "a") as f:
                    f.write(f"{t}\n")
                    f.close()
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
                    continue
                print(f"[WARNING] Intento {intento + 1} fallido: {e}")
                time.sleep(2 ** intento)
                if intento >= 9:
                    intento += 1
    
def main(email:str, password:str, tries:int, problem_id:str):

    # Initialize the GenAI client
    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
    compiler_id = "Python3"
    model = "gemini-2.5-flash"

    # Login to Jutge
    j = jutge.JutgeApiClient()
    j.login(email, password)
    success_number = 0.0
    problem_id = problem_id[0]
    for i in range(tries):
        analysis_mean = 0.0

        intento = 0
        while True:
            try:
                statement = j.problems.get_text_statement(str(problem_id))
                break

            except Exception as e:
                print(f"[ERROR] No se pudo obtener el enunciado del problema {problem_id}: {e}")
                time.sleep((2 ** intento))
                if intento >= 10:
                    intento += 1

        prompt = f"""
        Write a Python program to solve this problem:
        {statement}

        Take into account:
        - that the program have to eventually close its input reading.
        - that your output has to be a program that compiles and runs without errors, not a single extra character.
        - that the program has to be efficient and optimized, because the test has time limits.
        - that the inputs will eventually try to make your program fail, so consider edge cases and make the program to never get stuck in an infinite loop.
        Do not include any explanations, only the code.
        """

        answer = ask_for_solution(client, model, prompt)
        program = answer.replace("```", "")
        program = program.replace("python", "")
        '''
        os.makedirs(f"./SOLVING/{problem_id}/", exist_ok=True)
        with open(f"./SOLVING/{problem_id}/{i}.py", "w") as f:
            f.write(program)
            print(f"Program saved to ./SOLVING/{problem_id}/{i}.py")

        
        with open(f"./SOLVING/{problem_id}/{i}.py", "r") as f:
            intento = 0
            submission_out = None
            while True:
                try:
                    existing_submissions = j.student.submissions.index_for_problem(problem_id)
                    active_submission = None
                    for sub_id, sub in existing_submissions.items():
                        if sub.state in ("queued"):
                            active_submission = sub
                            break

                    if active_submission:
                        submission_out = active_submission
                        break
                    else:
                        submission_in = jutge.NewSubmissionIn(problem_id=problem_id, compiler_id=compiler_id, annotation="")
                        submission_out = j.student.submissions.submit_full(submission_in, f)
                        break
                
                except Exception as e:
                    print(f"[ERROR] No se pudo enviar la solución para el problema {problem_id}: {e}")
                    time.sleep((2 ** intento))
                    if intento <= 10:
                        intento += 1

            while True:
                submission = j.student.submissions.get(problem_id, submission_out.submission_id)
                print(f"Estado de la solución: {submission.veredict}")
                if submission.veredict not in ("Running", "Pending", None, ""):
                    print(f"Resultado final: {submission.veredict}")
                    break
                time.sleep(3)
        

        analysis_score = analyze(f"./SOLVING/{problem_id}/{i}.py")
        open(f"./SOLVING/{problem_id}/{i}_analysis.txt", "w").write(f"Analysis score: {analysis_score}\n")
        analysis_mean += analysis_score
        '''

    j.logout()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Genera soluciones para problemas de Jutge.")
    parser.add_argument("email", help="Email de Jutge")
    parser.add_argument("password", help="Contraseña de Jutge")
    parser.add_argument("tries", type=int, help="Número de intentos por problema")
    parser.add_argument("problems", nargs="+", help="Lista de IDs de problemas a resolver")
    args = parser.parse_args()
    main(args.email, args.password, args.tries, args.problems)