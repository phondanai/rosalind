from typing import List


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


dna_string, sequence_string = extract_fasta('rosalind_sseq.txt')

sequence_list = []
for c in sequence_string:
    sequence_list.append([ idx+1 for idx, i in enumerate(dna_string) if i == c ])

result = [sequence_list[0][0]]

for i in range(1, len(sequence_list)):
    tmp = [ i for i in sequence_list[i] if i > result[-1]][0]
    result.append(tmp)

print(' '.join(map(str,result)))

