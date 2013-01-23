import collections

f = open('rosalind_dna.txt', 'r')
DNA = f.readline()
f.close()

cnt = collections.Counter(DNA)

print ' '.join([str(v) for k, v in sorted(cnt.iteritems())])
