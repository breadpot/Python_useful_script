#!/usr/bin/env python
# -*- coding: UTF-8 -*- 
import random
import sys
d = open('./random.fna','w')
def simulate_sequence(length):
    dna = ['A', 'C', 'G', 'T']
    sequence = ''
    for i in range(length):
        sequence += random.choice(dna)
    return sequence

setsize = int(sys.argv[1])
minlength = int(sys.argv[2])
maxlength = int(sys.argv[3])

rlength = []
sequenceset = []
for i in range(setsize):
    rlength.append(random.randint(minlength, maxlength))

for length in rlength:
    sequenceset.append(simulate_sequence(length))

for sequence in sequenceset:
    print >> d, sequence,
#    for line2 in sequence:
#    print >> d, line2,
