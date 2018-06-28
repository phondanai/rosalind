from itertools import permutations


with open('rosalind_lexf.txt', 'r') as f:
    text_input = f.read().strip().split('\n')
    string, lenght = ''.join(text_input[0].split()), int(text_input[1])


string_list = []
for i in permutations(string*lenght, lenght):
    tmp_str = ''.join(map(str,i))
    if tmp_str not in string_list:
        string_list.append(tmp_str)

string_list.sort()

for i in string_list:
    print(i)
