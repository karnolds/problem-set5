
# Overview
For this problem set you will write a series of python programs to perform
sequence analysis tasks. Please edit this document to include your answers and
include your scripts in your pull request.  

## Problem 1
Write a python program that reports the number of intervals for each
chromosome in a bed file. Write the program as a python script named
``problem_1.py``. 

Execute your program on the ``data-sets/bed/lamina.bed`` file:

```bash
python3 problem_1.py lamina.bed
```

Which chromosome has the most intervals?
``chr3``

## Problem 2
Write a python program that parses a fastq file and determines the total number
of ``C`` bases in the fastq. Write the program as a python script named
``problem_2.py``.

Execute your program on the ``data-sets/fastq/SP1.fq`` file.

```bash
python3 problem_2.py SP1.fq
```

What is the total number of ``C`` bases?
``2046``

## Problem 3:
Write a python program that parses a fastq file and determines the most
common 6-mer (aka hexamer) sequence at the 5' and also the 3' end of each read. 
Write the program as a python script named ``problem_3.py``

What is the most common hexamer at the 5' end?
``CCCCCC``

What is the most common hexamer at the 3' end?
``ACCCCC``

## Problem 4:

The ``pysam`` package makes it easy to parse through a ``bam`` file
and extract important attributes. For this problem write a python program
named ``problem_4.py`` that parses a bam file and reports the following metrics: 
    
1. The total number of alignments on the positive and the negative strand. 
Use the Sam Flag attribute to determine if the alignment is on the forward or reverse
strand. 16 indicates an alignment on the reverse strand and 0 defines positive 
for this experiment. (hint: use the ``.flag`` attribute of an ``AlignedSegment``). More
information about these Flags in section 1.4 of the SAM [specification](http://samtools.github.io/hts-specs/SAMv1.pdf) 
    
2. The total number of alignments with no mismatches and the number of alignments
with more than zero mismatches. The NM tag records the edit distance between
the sequence and the reference. (hint: use the ``.get_tag()`` method to extract
the ``NM`` tag value). 

FYI to view the contents of a bam file as plain-text, use samtools view:

```bash
samtools view file.bam | less
```

How many positive strand aligned reads are there?
``your answer here``

How many negative strand aligned reads?
``your answer here``

How many alignments with no mismatches?
``your answer here``

How many alignments with more than zero mismatches?
``your answer here``


# problem_1.py
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

# problem_2.py
import sys

filename = ("/Users/katiearnolds/data-sets/fastq/SP1.fq")
fqfile = filename

def main():
  if len(sys.argv) != 2:
    print("need name of fq file to parse!")
    sys.exit(1)
    
  filename = sys.argv[1]
  
  num_C = 0
  
  with open(filename, "r") as fqfile:
    for lineno, line in enumerate(fqfile):
      if lineno %4 != 1:
        continue
      num_C += len([1 
                    for character in line
                    if character == 'C'])
#      for character in line:
#        if character == 'C':
#          num_C +=1

  print(num_C)
      

if __name__ == "__main__":
  main()

#problem_3.py
import sys
import operator

def main():
  if len(sys.argv) != 2:
    print("need name of fq file to parse!")
    sys.exit(1)
    
  filename = sys.argv[1]
  
  starting_hexamers = {}
  ending_hexamers = {}
  
  with open(filename, "r") as fqfile:
    for lineno, line in enumerate(fqfile):
      line = line.strip()
      if lineno %4 != 1:
        continue

      starting_hexamer = line[:6]
      if starting_hexamer in starting_hexamers:
        starting_hexamers[starting_hexamer] += 1
      else:
        starting_hexamers[starting_hexamer] = 1

      ending_hexamer = line[-6:]
      if ending_hexamer in ending_hexamers:
        ending_hexamers[ending_hexamer] += 1
      else:
        ending_hexamers[ending_hexamer] = 1

        
    print(max(starting_hexamers.iteritems(), key=operator.itemgetter(1))[0])
    print(max(ending_hexamers.iteritems(), key=operator.itemgetter(1))[0])



if __name__ == "__main__":
  main()
  
#problem_5.py
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
