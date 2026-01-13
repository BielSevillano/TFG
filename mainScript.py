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
import argparse

def main(tries: int, email:str, password:str, max_reviews:int,
         nproblems:int):
    
    problems_list = []
    with open("problems.txt", "w") as f:
        with open("./DENDROGRAMA/solucions.txt", "r") as text_file:
            lines = text_file.readlines()
            i = 0
            if nproblems == 0:
                for i in range(len(lines)):
                    if lines[i].split()[0] not in problems_list:
                        problems_list.append(lines[i].split()[0])
            else:
                for _ in range(nproblems):
                    while (lines[i].split()[0] in problems_list):
                        i += 1
                    problems_list.append(lines[i].split()[0])
        problems_list.append("CHANGE")
        with open("./DENDROGRAMA/solucionsPRO1.txt", "r") as text_file:
            lines = text_file.readlines()
            i = 0
            if nproblems == 0:
                for i in range(len(lines)):
                    if lines[i].split()[0] not in problems_list:
                        problems_list.append(lines[i].split()[0])
            else:
                for _ in range(nproblems):
                    while (lines[i].split()[0] in problems_list):
                        i += 1
                    problems_list.append(lines[i].split()[0])
        for problem in problems_list:
            f.write(problem + "\n")
    
    
    print("starting with feedback requests...")
    subprocess.run(["python3", "feedbackScript.py", email, password, str(tries), str(max_reviews)], check=True)
    
    print("starting with solving requests...")
    
    with open("problems.txt", "r") as f:
        problems = f.readlines()
        for problem_id in problems:
            problem_id = problem_id.strip()
            if problem_id == "CHANGE":
                continue
            print(f"Solving problem {problem_id}...")
            try:
                subprocess.run(["python3", "solvingScript.py", email, password, str(tries), problem_id], check=True)
            except subprocess.CalledProcessError as e:
                print(f"[ERROR] Error al resolver el problema {problem_id}: {e}")          
    
    j = jutge.JutgeApiClient()
    j.login(email, password)
    compiler_id = "Python3"

    with open("problems.txt", "r") as f:
        problems = f.readlines()
        for problem_id in problems:
            problem_id = problem_id.strip()
            if problem_id == "CHANGE":
                continue
            print(f"Sending submissions for problem {problem_id}...")
            for i in range(tries):
                if not os.path.exists(f"./SOLVING/{problem_id}/{i}.py"):
                    print(f"[WARNING] No se encontró la solución para el problema {problem_id}, intento {i}.")
                    continue
                else:
                    print(f"Sending submission for problem {problem_id}, attempt {i}...")
                    submission_in = jutge.NewSubmissionIn(problem_id=problem_id, compiler_id=compiler_id, annotation="")
                    submission_out = j.student.submissions.submit_full(submission_in, f)
    

    max_time = 0.0
    min_time = float('-inf')
    with open("time_log_feedback.txt", "r") as log_file:
        lines = log_file.readlines()
        for line in lines:
            if (len(line.split(" "))) > 1:
                continue
            time_taken = float(line.strip())
            if time_taken < max_time:
                max_time = time_taken
            if time_taken > min_time:
                min_time = time_taken
        print(f"Max feedback time: {max_time} seconds")
        print(f"Min feedback time: {min_time} seconds")
    
    with open("time_log_feedback.txt", "a") as log_file:
        log_file.write(f"Max feedback time: {max_time} seconds\n")
        log_file.write(f"Min feedback time: {min_time} seconds\n")
    
    max_time = 0.0
    min_time = float('-inf')

    with open("time_log_solving.txt", "r") as log_file:
        lines = log_file.readlines()
        for line in lines:
            if (len(line.split(" "))) > 1:
                continue
            time_taken = float(line.strip())
            if time_taken < max_time:
                max_time = time_taken
            if time_taken > min_time:
                min_time = time_taken
        print(f"Max solving time: {max_time} seconds")
        print(f"Min solving time: {min_time} seconds")
    
    with open("time_log_solving.txt", "a") as log_file:
        log_file.write(f"Max solving time: {max_time} seconds\n")
        log_file.write(f"Min solving time: {min_time} seconds\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Script principal.")
    parser.add_argument("tries", type=int, help="Número de intentos por problema")
    parser.add_argument("email", help="Email de Jutge")
    parser.add_argument("password", help="Contraseña de Jutge")
    parser.add_argument("max_reviews", type=int, help="Número máximo de soluciones por problema")
    parser.add_argument("nproblems", type=int, help="Número de problemas a seleccionar por archivo")
    args = parser.parse_args()
    main(args.tries, args.email, args.password, args.max_reviews, args.nproblems)





