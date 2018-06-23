import sys
from typing import Dict
from pprint import pprint
import operator

fasta_file = sys.argv[1]

def calculate_gc(dna_string: str) -> float:

    C = dna_string.count('C')
    G = dna_string.count('G')
    dna_lenght = len(dna_string)

    results = ((C + G) / dna_lenght) * 100

    return results


def gen_fasta_dict(fasta_file: str) -> Dict:

    with open(fasta_file, 'r') as f:
        fasta_id_list = []

        for line in f:
            if line.startswith('>'):
                fasta_id_list.append(line[1:].rstrip())


    with open(fasta_file, 'r') as f:
        results = []
        tmp_str = ''
        start = True
        for line in f:
            if not line.startswith('>'):
                tmp_str += line.rstrip()
            elif start:
                start = False
                continue
            else:
                results.append(tmp_str)
                tmp_str = ''
        else:
            results.append(tmp_str)

    print(fasta_id_list)
    print(results)

    fasta_dict = {fasta_id: fasta_string for fasta_id, fasta_string in zip(fasta_id_list, results)}

    return fasta_dict


if __name__ == '__main__':
    fasta_dict = gen_fasta_dict(fasta_file)
    highest = max(fasta_dict, key=lambda k: calculate_gc(fasta_dict[k]))
    print(highest)
    print(calculate_gc(fasta_dict[highest]))
