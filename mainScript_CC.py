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
    subprocess.run(["python3", "feedbackScript_CC.py", email, password, str(tries), str(max_reviews)], check=True)
                    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Script principal.")
    parser.add_argument("tries", type=int, help="Número de intentos por problema")
    parser.add_argument("email", help="Email de Jutge")
    parser.add_argument("password", help="Contraseña de Jutge")
    parser.add_argument("max_reviews", type=int, help="Número máximo de soluciones por problema")
    parser.add_argument("nproblems", type=int, help="Número de problemas a seleccionar por archivo")
    args = parser.parse_args()
    main(args.tries, args.email, args.password, args.max_reviews, args.nproblems)





