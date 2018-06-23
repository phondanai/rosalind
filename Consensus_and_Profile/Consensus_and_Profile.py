import sys
from collections import Counter
from pprint import pprint


fasta_file = sys.argv[1].strip()

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


def create_table(matrix):
    lenght = len(matrix[0])
    results = []

    for idx in range(lenght):
        results.append([elm[idx] for elm in matrix])

    results = [''.join(i) for i in results]

    return results


def report(table):
    print('Report')
    print(''.join([Counter(i).most_common(1)[0][0] for i in table]))

    for c in 'ACGT':
        count = [str(i.count(c)) for i in table]
        print(c+':',' '.join(count))

print(results)
table = create_table(results)
print(table)

report(table)
