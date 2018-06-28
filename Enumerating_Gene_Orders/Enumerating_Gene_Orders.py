from itertools import permutations

with open('rosalind_perm.txt', 'r') as f:
    input_num = int(f.read().strip())

result = []

def gen_num_list(input_num):
    return [i for i in range(1, (input_num+1))]

num_list = gen_num_list(input_num)

result = [i for i in permutations(num_list) ]

print(len(result))

for i in result:
    print(" ".join(map(str, i)))
