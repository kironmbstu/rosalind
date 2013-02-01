#!/usr/bin/env python

# The probabilities of having an offspring showing the dominant factor are the
# following ones:
#
# AA-AA = 1
# AA-Aa = 1
# AA-aa = 1
# Aa-Aa = 0.75
# Aa-aa = 0.5
# aa-aa = 0
#
# And as they will have two descendants, the values are multiplied by two

probs = [2., 2., 2., 1.5, 1, 0]

with open('rosalind_iev.txt', 'r') as f:
    couples = map(int, f.readline().split())

print sum([a*b for a, b in zip(probs, couples)])