def cons(strings):
    from collections import Counter
    counters = map(Counter, zip(*strings))
    consensus = "".join(c.most_common(1)[0][0] for c in counters)
    profile_matrix = "\n".join(b + ": " + \
        " ".join(str(c[b]) for c in counters) for b in "ACGT")
    return consensus + "\n" + profile_matrix

with open('example.txt') as f:
    strings = []
    [strings.append(DNA.rstrip()) for DNA in f.readlines()]
    print cons(strings)
