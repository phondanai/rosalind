from urllib.request import urlopen


with open('rosalind_dbpr.txt', 'r') as f:
    uniprot_id = f.read().strip()

resp = urlopen('http://www.uniprot.org/uniprot/{}.txt'.format(uniprot_id))

uniprot_text = resp.read().decode('utf-8')
uniprot_list = uniprot_text.split('\n')

dna_list = [i for i in uniprot_list if "GO;" in i]

protein_result = [i.split(';')[2].strip()[2:] for i in dna_list if 'P:' in i]

for i in protein_result:
    print(i)

