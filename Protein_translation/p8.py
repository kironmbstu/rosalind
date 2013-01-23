def codon_table():
    """Code to generate a codon translation table.
    Returns a ditc in which the key is the three 3-nucleobase string and the
    value is the corresponding translation symbol (aminoacid).
    """
    f = open('codon_table.txt', 'r')
    codontable = f.readlines()
    f.close()
    c = dict()
    for k, v in [elem.split() for elem in codontable]:
        c[k] = v
    return c

f = open('rosalind_prot.txt', 'r')
rna = f.readline()
f.close()

rna = rna.rstrip()
protein = []
codon = codon_table()
for i in range(0, len(rna), 3):
    protein.append(codon[rna[i:i+3]])
print ''.join(protein[:-1])
