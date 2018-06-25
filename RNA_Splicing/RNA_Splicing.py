from typing import List

from pprint import pprint
from typing import Dict


table = {
        'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
        'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
        'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
        'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
        'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
        'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
        'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
        'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
        'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
        'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
        'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
        'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
        'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
        'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
        'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
        'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',
}

def make_rna_dict(rna_code_list):
    rna_code_dict = {}
    rna_code_dict = { i[:3]:str.strip(i[3:]) for i in rna_code_list}

    return rna_code_dict


def protein_lookup(rna_code_dict: Dict, rna_code: str) -> str:

    return rna_code_dict.get(rna_code)



def extract_fasta(fasta_file: str) -> List:

    results = []

    with open(fasta_file, 'r') as f:
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

    return results


def replace_with_zeros(dna_string, intron):
    results = dna_string.replace(intron, '0'*len(intron))

    return  results


dna_string, *introns = extract_fasta('rosalind_splc.txt')

for intron in introns:
    replaced = replace_with_zeros(dna_string, intron)
    dna_string = replaced

results = dna_string.replace('0', '')

if __name__ == '__main__':

    results = [protein_lookup(table, results[i:3+i]) for i in range(0, len(results), 3)]

    print(''.join(results[:results.index('_')]))

