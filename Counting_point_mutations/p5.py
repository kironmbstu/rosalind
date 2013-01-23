def hamming(s1, s2):
    assert len(s1) == len(s2)
    return sum(c1 != c2 for c1, c2 in zip(s1, s2))

f = open('rosalind_hamm.txt', 'r')
dnas = f.readlines()
f.close()

print hamming(dnas[0].rstrip(), dnas[1].rstrip())
