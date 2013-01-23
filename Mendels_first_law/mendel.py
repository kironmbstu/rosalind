"""
Three positive integers k, m, and n, representing a population containing k+m+n organisms: 
k t are homozygous dominant for a factor, m are heterozygous, and n are homozygous recessive.
Return the probability that two randomly selected mating organisms 
will produce an individual possessing a dominant allele
"""

f = open('rosalind_mendel.txt', 'r')
sets = f.readlines()
f.close()

for population in sets:
    k, m, n = map(float, population.split())
    t = k+m+n
    pk = k/t
    pm = m/t
    pn = n/t

    print (pk*pk) + (pk*pm)*2 + (pk*pn)*2 + (0.5*pm*0.5*pm) + (0.75*pm*pm)*2 + (0.5*pm*pn)*2
