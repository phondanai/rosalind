import re
import urllib.request
import sys
import time


def get_protein_fasta(uniprot_id: str) -> str:

    DATA_URL = 'http://www.uniprot.org/uniprot/{}.fasta'.format(uniprot_id)
    with urllib.request.urlopen(DATA_URL) as f:
        protein_sequence = f.read()

    return protein_sequence


def get_protein_string(fasta):
    protein_string = ''.join(str(fasta).split('\\n')[1:-1])

    return protein_string


def protein_motif(uniprot_id: str) -> str:
    protein_sequence = get_protein_fasta(uniprot_id)
    protein_string = get_protein_string(protein_sequence)

    pattern = '(?=(N[^P][ST][^P]))'
    prog = re.compile(pattern)


    if prog.finditer(protein_string):
        results = ' '.join([ str(loc.start()+1) for loc in prog.finditer(protein_string) ])
    else:
        return


    return uniprot_id, results


if __name__ == '__main__':
    # finding individual motif
    if len(sys.argv) == 2:
        uniprot_id, motif = protein_motif(sys.argv[1])
        if motif:
            print(uniprot_id)
            print(motif)
        sys.exit()

    with open('rosalind_mprt.txt', 'r') as f:
        lst = f.read().strip().split('\n')

    for i in lst:
        uniprot_id, motif = protein_motif(i)
        if motif:
            print(uniprot_id)
            print(motif)
        time.sleep(1)

