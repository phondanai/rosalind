import sys

str_1, str_2 = sys.argv[1].strip(), sys.argv[2].strip()

print(len([(i,v) for (i,v) in zip(str_1, str_2) if i != v]))

