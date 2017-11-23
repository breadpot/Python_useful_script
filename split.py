#!/usr/bin/env python
# -*- coding: UTF-8 -*- 
# -*- coding: cp936 -*-

import re
import os
import string
import sys

#f = open(r'','r')
#d = open('','w')
FASTA= sys.argv[1]
fasta= open(FASTA, 'U')

OUTPUT= sys.argv[2]
output= open(OUTPUT,"w")

for line in fasta.readlines():
    line2 = re.sub(r"(?<=\w)(?=(?:\w\w)+$)", " ", line)
    print >> output, line2,
