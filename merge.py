#!/usr/bin/env python
#_*_coding:utf-8_*_
import itertools
import sys
import re

TXT1= sys.argv[1]
txt1= open(TXT1, 'U')

TXT2= sys.argv[2]
txt2= open(TXT2, 'U')

OUTPUT= sys.argv[3]
#output= open(OUTPUT,"w")

#string1= sys.argv[4]
#string2= str(string1)

#with open(r'') as f:
txt1_1=[r.rstrip("\n") for r in txt1.readlines()]
#with open(r'') as f:
txt2_1=[r.rstrip("\n") for r in txt2.readlines()]

result=itertools.izip_longest(txt1_1,txt2_1,fillvalue=' ')
#print(result)

with open(OUTPUT,"w+") as output:
    [output.write("\t".join(r)+"\n") for r in result]
