import re
from Bio import SeqIO

def pattern(DNA):
    r = r"^%s"
    return re.compile(r % str(DNA[-3:]))

if __name__=="__main__":
    DNAs = []
    f = open('rosalind_grph.txt', 'r')
    [DNAs.append((i.id, i.seq.tostring())) for i in SeqIO.parse(f, 'fasta')]
    f.close()
    
    for i in range(len(DNAs)):
        r = pattern(DNAs[i][1])
        for j in range(len(DNAs)):
            if i != j:
                if r.match(DNAs[j][1]):
                    print ' '.join([DNAs[i][0], DNAs[j][0]])