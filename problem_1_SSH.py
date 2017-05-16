#! /usr/bin/env python3  

from collections import Counter

data_file = ("/Users/katiearnolds/data-sets/bed/lamina.bed")

counts = Counter()
 
for line in open(data_file):
  if line.startswith('#'): continue
  fields = line.split('\t')
  chrom = fields[0]
  counts[chrom] += 1
    
for chrom, count in counts.items():
  sortme = [(v,k) for k,v in counts.items()]
  sortme.sort()
  sortme.reverse()
print (sortme[0] [1])






