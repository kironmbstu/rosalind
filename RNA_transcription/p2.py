import re

f = open('rosalind_rna.txt', 'r')
DNA = f.readline()
f.close()

rna = re.sub('T', 'U', DNA)
print rna
