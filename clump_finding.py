"""
Now imagine that you are trying to find ori in a newly sequenced 
bacterial genome. Searching for “clumps” of "ATGATCAAG"/"CTTGATCAT" or 
"CCTACCACC"/"GGTGGTAGG" is unlikely to help, since this new genome may use 
a completely different hidden message! Before we lose all hope, let’s 
change our computational focus: instead of finding clumps of a specific 
k-mer, let’s try to find every k-mer that forms a clump in the genome. 
Hopefully, the locations of these clumps will shed light on the location 
of ori.

Our plan is to slide a window of fixed length L along the genome, looking 
for a region where a k-mer appears several times in short succession. 
The parameter value L = 500 reflects the typical length of ori in 
bacterial genomes.

We think of a k-mer as a “clump” if it appears many times within a short 
interval of the genome. More formally, given integers L and t, a k-mer 
Pattern forms an (L, t)-clump inside a (longer) string Genome if there 
is an interval of Genome of length L in which this k-mer appears at least 
t times. (This definition assumes that the k-mer completely fits within 
the interval.) 
"""

