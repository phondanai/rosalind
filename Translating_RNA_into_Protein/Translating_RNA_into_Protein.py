from pprint import pprint
from typing import Dict


RNA_CODE_TABLE = """UUU F      CUU L      AUU I      GUU V
UUC F      CUC L      AUC I      GUC V
UUA L      CUA L      AUA I      GUA V
UUG L      CUG L      AUG M      GUG V
UCU S      CCU P      ACU T      GCU A
UCC S      CCC P      ACC T      GCC A
UCA S      CCA P      ACA T      GCA A
UCG S      CCG P      ACG T      GCG A
UAU Y      CAU H      AAU N      GAU D
UAC Y      CAC H      AAC N      GAC D
UAA Stop      CAA Q      AAA K      GAA E
UAG Stop      CAG Q      AAG K      GAG E
UGU C      CGU R      AGU S      GGU G
UGC C      CGC R      AGC S      GGC G
UGA Stop      CGA R      AGA R      GGA G
UGG W      CGG R      AGG R      GGG G"""


def make_rna_dict(rna_code_list):
    rna_code_dict = {}
    rna_code_dict = { i[:3]:str.strip(i[3:]) for i in rna_code_list}

    return rna_code_dict


def protein_lookup(rna_code_dict: Dict, rna_code: str) -> str:

    return rna_code_dict.get(rna_code)


if __name__ == '__main__':
    newline_split = RNA_CODE_TABLE.split('\n')
    spaces_split = [i.split(' '*6) for i in newline_split]

    spaces_split = [y for x in spaces_split for y in x]
    #pprint(spaces_split)

    rna_code_dict = make_rna_dict(spaces_split)

    with open('rosalind_prot.txt', 'r') as f:
        rna_string = f.read()

    #pprint(rna_code_dict)
    #pprint([rna_string[i:3+i] for i in range(0, len(rna_string), 3)])

    results = [protein_lookup(rna_code_dict, rna_string[i:3+i]) for i in range(0, len(rna_string), 3)]
    print(''.join(results[:results.index('Stop')]))
