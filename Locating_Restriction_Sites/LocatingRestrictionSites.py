from typing import List
from pprint import pprint
import sys


def complement_(string: str) -> str:
    in_table = 'ACGT'
    out_table = 'TGCA'

    trantab = str.maketrans(in_table, out_table)

    result = string.translate(trantab)

    return result


def reverse_string_(string: str) -> str:
    return string[::-1]


def is_dna(string: str) -> bool:

    return string == complement_(reverse_string_(string))


def sliding_(string: str, window: int) -> List[str]:
    last = len(string) - window
    window_ = window
    results = []

    for idx, _ in enumerate(string):
        if idx > last:
            break
        results.append([idx, window, string[idx:(idx+window)]])

    return results


def read_fasta(fasta_file: str) -> str:
    with open(fasta_file, 'r') as f:
        tmp = f.read()

    result = ''.join(tmp.split('\n')[1:-1])

    return result


fasta_file = sys.argv[1].strip()
string = read_fasta(fasta_file)

results = []
for i in range(4,13):
    palindrome = sliding_(string, i)
    for i,w,string in palindrome:
        if is_dna(string):
            #print(i+1, '\t', w,'\t', string)
            results.append([i+1,w])

results.sort(key=lambda res: res[0])

for i,v in results:
    print(i,v)

