# Problem
A common substring of a collection of strings is a substring of every member of
the collection. We say that a common substring is a longest common substring if
there does not exist a longer common substring. For example, "CG" is a common 
substring of "ACGTACGT" and "AACCGGTATA", but it is not as long as possible; in
this case, "GTA" is a longest common substring of "ACGTACGT" and "AACCGTATA".

Note that the longest common substring is not necessarily unique; for a simple
example, "AA" and "CC" are both longest common substrings of "AACC" and "CCAA".

__Given:__ A collection of k (k≤100) DNA strings of length at most 1 kbp each in
FASTA format.

__Return:__ A longest common substring of the collection. (If multiple solutions
exist, you may return any single solution.)

##Strategy to follow
[Suffix trees](http://en.wikipedia.org/wiki/Suffix_tree) seems to be the more 
general and efficient solution for this problem. As the number of DNA strings to
compare and its size aren't very large, one could think on a brute force algorithm.
However, I'll try to implements a SuffixTree class using efficient memory management.
 