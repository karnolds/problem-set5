#! /usr/bin/env python3  

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
