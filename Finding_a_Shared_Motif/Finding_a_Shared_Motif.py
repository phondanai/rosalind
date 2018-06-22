import sys


def gen_permu(string):
    #results = [string[:i+1] for i,_ in enumerate(string)]
    results = []
    for i in range(len(string)):
        results.append([string[i:j+1] for j,_ in enumerate(string)])

    return results

permu_lst = []
for string in ["GATTACA", "TAGACCA", "ATACA"]:
    permu_lst.append(gen_permu(string))
    break

print(permu_lst)
#print(set(permu_lst[0]) , set(permu_lst[1]) , set(permu_lst[2]))
