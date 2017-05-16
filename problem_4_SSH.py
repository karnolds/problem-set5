#! /usr/bin/env python3  

import sys
import operator
from collections import Counter
import pysam



def main():
  if len(sys.argv) != 2:
    sys.exit(1)
    
  filename = sys.argv[1]
  
bamfile = AlignmentFile (filename)

counts = 0
strands = counter ()
mistmatches = counter ()

for record in bamfile:
  strand = record.flag
  strands[strand] += 1
  
if strand == 0:
  print("Pos_strand_alignments:", count)
  
if strand == 16:
  print("Negative strand alignments:", count)




  
 
