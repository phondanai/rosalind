from typing import Dict
from pprint import pprint
from collections import OrderedDict

#def gen_fasta_dict(fasta_file: str) -> Dict:
#
#    with open(fasta_file, 'r') as f:
#        data = f.read().strip().split('\n')
#
#    fasta_dict = OrderedDict()
#
#    data_iter = iter(data)
#
#    for item in data_iter:
#        fasta_dict[item[1:]] = next(data_iter)
#
#    return fasta_dict

def gen_fasta_dict(fasta_file: str) -> Dict:

    with open(fasta_file, 'r') as f:
        fasta_id_list = []

        for line in f:
            if line.startswith('>'):
                fasta_id_list.append(line[1:].rstrip())


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

#    print(fasta_id_list)
#    print(results)

    fasta_dict = {fasta_id: fasta_string for fasta_id, fasta_string in zip(fasta_id_list, results)}

    return fasta_dict


def get_all_edges(fasta_dict):
    item_name_list = fasta_dict.keys()

    item_name_list = list(item_name_list)

    for i, v in enumerate(item_name_list):
        tmp_list = item_name_list[:]
        tmp_key = tmp_list.pop(i)
        for remain in tmp_list:
            if fasta_dict[tmp_key][-3:] == fasta_dict[remain][:3]:
                print(tmp_key, remain)

    return None

fasta_dict = gen_fasta_dict('rosalind_grph.txt')
#pprint(fasta_dict)

get_all_edges(fasta_dict)
