import sys
from pprint import pprint
from typing import Dict, List
import operator
from functools import reduce


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

    fasta_dict = {fasta_id: fasta_string for fasta_id, fasta_string in zip(fasta_id_list, results)}

    return fasta_dict

def sliding_(string: str, window: int) -> List[str]:
    last = len(string) - window
    window_ = window
    results = []

    for idx, _ in enumerate(string):
        if idx > last:
            break
        results.append([string[idx:(idx+window)]])

    return results


def flatten(items):
    for i in items:
        if isinstance(i, list):
            yield from flatten(i)
        else:
            yield i


def longest_common_string(min_lenght, dna_strings):

    candidates = []
    for i in range(1, len(min_lenght)+1):
        combination = sliding_(min_lenght, i)
        candidates.append(combination)

    candidates = list(flatten(candidates))

    result = []
    for c in candidates:
        contains = all(c in string for string in dna_strings)
        if contains:
            result.append(c)

    return max(result, key=len)


if __name__ == '__main__':
    fasta_dict = gen_fasta_dict('rosalind_lcsm.txt')

    min_lenght = min([v for v in fasta_dict.values()], key=len)
    dna_strings = [v for v in fasta_dict.values()]

    min_lenghts = [v for v in fasta_dict.values() if len(v) == len(min_lenght)]

    if len(min_lenghts) != 1:
        min_lenght = longest_common_string(min_lenght, min_lenghts)

    print(longest_common_string(min_lenght, dna_strings))

