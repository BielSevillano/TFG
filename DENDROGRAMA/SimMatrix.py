from base64 import b64decode
import os
import csv
import torch
from transformers import AutoTokenizer, AutoModel
import argparse
from base64 import b64decode
import numpy as np

MODEL_NAME = "microsoft/codebert-base"
MAX_LENGTH = 512

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModel.from_pretrained(MODEL_NAME)

def embed_code(code: str) -> torch.Tensor:
    inputs = tokenizer(code, return_tensors="pt", truncation=True, max_length=MAX_LENGTH)
    with torch.no_grad():
        outputs = model(**inputs)
        return outputs.last_hidden_state.mean(dim=1)

def cosine_similarity(a: torch.Tensor, b: torch.Tensor) -> float:
    return torch.nn.functional.cosine_similarity(a, b).item()

def main(problem_id: str, max_reviews: int, solutions_path: str, output_csv: str):

    embeddings = {}
    decoded_programs = []

    with open(solutions_path, "r", encoding="latin-1") as f:
        lines = f.readlines()
        i = 0
        while (lines[i].split()[0] != problem_id):
            i += 1
        reviews = 0
        for idx, line in enumerate(lines[i + 1:], start=1):
            line = line.strip()
            if not line or line.split()[1] != "Python3":
                continue

            if reviews >= max_reviews:
                break

            # coger la última parte de la línea (el bloque base64)
            base64_code = line.split()[-1]

            try:
                decoded_bytes = b64decode(base64_code)
                decoded_text = decoded_bytes.decode("utf-8", errors="replace")

                decoded_programs.append(decoded_text)
                embeddings[line] = embed_code(decoded_text)

            except Exception as e:
                print(f"[ERROR] en línea {idx}: {e}")

            reviews += 1

    keys = list(embeddings.keys())
    # Similarity matrix
    n = len(embeddings)
    matrix = [[0.0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if i <= j: 
                sim = cosine_similarity(embeddings[keys[i]], embeddings[keys[j]])
                matrix[i][j] = sim
                matrix[j][i] = sim

    # Save decoded programs, rewrite file if exists
    if os.path.exists("./MATRICES/decoded_programs.npy"):
        os.remove("./MATRICES/decoded_programs.npy")
    np.save("./MATRICES/decoded_programs.npy", np.array(decoded_programs, dtype=object), allow_pickle=True)
    
    # CSV (open or create)
    with open(output_csv, mode="w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        for i in range(n):
            row = matrix[i]
            writer.writerow(row)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Genera una matriz de similitud entre archivos Python en una carpeta.")
    parser.add_argument("problem_id", help="ID del problema")
    parser.add_argument("max_reviews", type=int, help="Número máximo de revisiones a considerar")
    parser.add_argument("solutions_path", help="Ruta al archivo de soluciones")
    parser.add_argument("output_csv", default="./MATRICES/similarity_matrix.csv", help="Ruta del archivo CSV de salida")
    args = parser.parse_args()
    main(args.problem_id, args.max_reviews, args.solutions_path, args.output_csv)