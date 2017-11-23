#!/usr/bin/env python
# -*- coding: UTF-8 -*- 
# -*- coding: cp936 -*-

import re
import os
import string
import sys
import operator

FASTA= sys.argv[1]
f= open(FASTA, 'U')

OUTPUT= sys.argv[2]
d= open(OUTPUT,"w")

count_dict={}
for line in f.readlines():
    line = line.strip()
    count = count_dict.setdefault(line,0)
    count += 1
    count_dict[line] = count
sorted_count_dict = sorted(count_dict.iteritems(), key=operator.itemgetter(1), reverse=True)
for item in sorted_count_dict:
    #g="%s,%d"%(item[0],item[1])
    print >> d, "%s,%d"%(item[0],item[1])
