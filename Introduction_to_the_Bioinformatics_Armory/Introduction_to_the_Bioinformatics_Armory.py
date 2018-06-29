with open('rosalind_ini.txt', 'r') as f:
    data = f.read().strip()

print(' '.join(map(str, [data.count(c) for c in 'ACGT'])))
