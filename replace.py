#!/usr/bin/env python
# -*- coding: UTF-8 -*- 
# -*- coding: cp936 -*-
import sys
import re

FASTA= sys.argv[1]
fasta= open(FASTA, 'U')

OUTPUT= sys.argv[2]
output= open(OUTPUT,"w")

replace1= sys.argv[3]
replace2= sys.argv[4]

str1= str(replace1)
str2= str(replace2)

lines=fasta.readlines()

for l in lines:
    output.write(l.replace(str(replace1),str(replace2)))