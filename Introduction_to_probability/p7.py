f = open('rosalind_prob.txt', 'r')
A = f.readlines()
f.close()
A = A[0].rstrip().split()
B = []

for prob in A:
    PC = PG = (float(prob)/2)**2
    PT = PA = ((1-float(prob))/2)**2
    B.append(PC + PG + PA + PT)

print ' '.join([str(p) for p in B])
