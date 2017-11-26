#!/usr/bin/env python
# -*- coding: UTF-8 -*- 
# -*- coding: cp936 -*-
# usage example in terminal:python annotation3.py dic query (search text in "query" file for relationship in "dic" file)

import itertools
import re
import os
import string
import sys

RAWDIC= sys.argv[1]
QUERY= sys.argv[2]

rawdic = open(RAWDIC, 'U')
c = dict()
for line in rawdic:
	  line = line.strip().split(' ')
	  c[line[0]] = line[1]
rawdic.close()

input_file= open(QUERY, 'U')
output_file= open("temp2","w+")

line = input_file.readline()

while line:
	  f = line.split()
	  print(f)
	  res = []
	  for item in f:
	  	  res.append(c[(item)])
	  output_file.write(str(res)+ '\n')
	  line = input_file.readline()
          
input_file.close()
output_file.close()

with open(QUERY) as f:
    txt1_1=[r.rstrip("\n") for r in f.readlines()]
with open("temp2") as f:
    txt2_1=[r.rstrip("\n") for r in f.readlines()]

result=itertools.izip_longest(txt1_1,txt2_1,fillvalue=' ')

with open("temp3","w+") as output2:
    [output2.write("\t".join(r)+"\n") for r in result]

replace1= open("temp3", 'U')
replace2= open('final.out',"w")

lines=replace1.readlines()

for replace001 in lines:
    replace2.write(replace001.replace("['","").replace("']",""))

replace1.close()
replace2.close()

os.remove("temp2")
os.remove("temp3")
