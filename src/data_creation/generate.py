import random
import json
from tqdm import tqdm

NUM_SAMPLES   = 5000 
DATASET_SPLIT = "val"

nucleotides = ["A", "C", "G", "T"]
families = ["INS","HBB","TP53"]

# JSONL filename
jsonl_filename = f'{DATASET_SPLIT}.jsonl'

with open(jsonl_filename, 'w') as f:

    for sample_count in tqdm(range(NUM_SAMPLES), desc='Creating and saving samples'):
        sequence = []
        for char_count in range (150):
            sequence.append(random.choice(nucleotides))
        family = random.choice(families)
        json_line = json.dumps({'gene_subsequence': sequence, 'gene_family': family})
        f.write(json_line + '\n')

    print(f"Data saved as JSONL file: {jsonl_filename}")

