import re

f = open('rosalind_revc.txt', 'r')
dna = f.readline()
f.close()

sub = {           \
        'A':'T',  \
        'T':'A',  \
        'C':'G',  \
        'G':'C',  \
}

r_dna = ''

for base in dna[::-1]:
    try:
        base = sub[base]
    except KeyError:
        pass
    r_dna += base

print r_dna
