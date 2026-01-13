import argparse
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from scipy.cluster.hierarchy import linkage, dendrogram, fcluster
from scipy.spatial.distance import pdist, squareform
import matplotlib.pyplot as plt
import seaborn as sns
import subprocess
import os

SIM_MATRIX = "./MATRICES/similarity_matrix.csv"
DECODED_PROGRAMS = "./MATRICES/decoded_programs.npy"
OUTPUT_DIR = "./DENDROGRAMAS/"

def main(problem_id: str, max_reviews: int, solutions_path: str):
    with open(solutions_path, "r", encoding="latin-1") as f:
        with open("./solucions_relative.txt", "w", encoding="latin-1") as f_rel:
            lines = f.readlines()
            for line in lines:
                if line.split()[0] == problem_id and (line.split()[1] == "G++" or line.split()[1] == "P1++" or line.split()[1] == "G++11"):
                    f_rel.write(line)

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    subprocess.run(["python3", "SimMatrix.py", problem_id, str(max_reviews), "./solucions_relative.txt", "./MATRICES/similarity_matrix.csv"], check=True)
    data = pd.read_csv(SIM_MATRIX, header=None)
    programs = np.load(DECODED_PROGRAMS, allow_pickle=True)

    scaler = StandardScaler()
    data_scaled = scaler.fit_transform(data)

    lnks = linkage(data_scaled, method='complete', metric='euclidean')

    dendro_data = {
        'linkage': lnks,
        'programs': programs
    }

    output_path = os.path.join(OUTPUT_DIR, f"dendrogram_{problem_id}.npy")
    np.save(output_path, dendro_data, allow_pickle=True)

    dt = pd.DataFrame(data)
    print("DENDOGRAM GENERATED: {problem_id}, {max_reviews} reviews")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Genera una matriz de similitud entre archivos Python en una carpeta.")
    parser.add_argument("problem_id", help="ID del problema")
    parser.add_argument("max_reviews", type=int, help="Número máximo de revisiones aconsiderar")    
    parser.add_argument("solutions_path", help="Ruta al archivo de soluciones")
    args = parser.parse_args()
    main(args.problem_id, args.max_reviews, args.solutions_path)