f = open('rosalind_gc.txt', 'r')
raw_samples = f.readlines()
f.close()

samples = {}
cur_key = ''

for elem in raw_samples:
    if elem[0] == '>':
        cur_key = elem[1:].rstrip()
        samples[cur_key] = ''
    else:
        samples[cur_key] += elem.rstrip()

for s_id, s in samples.iteritems():
    samples[s_id] = (float(s.count('G') + s.count('C'))/len(s))*100

(s_id, gc) = max(list(samples.iteritems()), key = lambda item:item[1])
print s_id
print gc + '%'
