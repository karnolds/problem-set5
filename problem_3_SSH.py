#! /usr/bin/env python3  

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
