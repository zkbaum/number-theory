#!/usr/bin/env python

# FRINT 20.3
# This script helps in computing all the cubic residues for a couple primes

from util import is_prime

# CONFIG
LOWER_BOUND = 3
UPPER_BOUND = 20


for p in range(LOWER_BOUND,UPPER_BOUND):
    if is_prime(p):
        print("\n[Processing %d]\n----------------" % p)
        
        cubic_residues = []
        for i in range(1,p):
            blah = (i**3) % p
            if blah not in cubic_residues:
                cubic_residues.append(blah)
        cubic_residues.sort()
        # part a
        print(cubic_residues)
        # part c
        print("p mod 3: ", p%3)
