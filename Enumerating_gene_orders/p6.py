import itertools

f = open('resp.out', 'w')

n = int(raw_input("Insert n to calculate permutations of {1..n}: "))

perms = list(itertools.permutations(range(1, n+1)))
f.writelines(str(len(perms)) + '\n')
for p in perms:
    f.writelines(' '.join(str(elem) for elem in p) + '\n')
f.close()
