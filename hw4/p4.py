#!/usr/bin/env python

# FRINT 20.2
# This script helps with computing the sums of all the quadratic
# residues and nonresidues

from util import is_prime

# CONFIG
LOWER_BOUND = 3
UPPER_BOUND = 20


a_equal_b = []
for p in range(LOWER_BOUND,UPPER_BOUND):
    if is_prime(p):
        print("\n[Processing %d]\n----------------" % p)
        
        # Determine residues and NR
        residues = []
        nonresidues = []
        for i in range(1,int((p+1)/2)):
            residues.append(i*i % p)

        
        nonresidues=list(set(range(1,p))-set(residues))
        nonresidues.sort()
        residues.sort()
        # print("Residues:",residues)
        # print("Nonresidues:",nonresidues)

        A = sum(residues)
        B = sum(nonresidues)
        if (A==B):
            a_equal_b.append(p)
        print("A:", A)
        print("B:", B)
        # print("A+B:", A+B)
        # print("p(p-1)/2:", p*(p-1)/2)
        print("A mod p:", A%p)
        print("B mod p:", B%p)


# PART D
# for x in a_equal_b:
    # print("------")
    # print(x%2)
    # print(x%3)
    # print(x%4)
    # print(x%5)
# all_primes = [x for x in range(LOWER_BOUND,UPPER_BOUND) if is_prime(x)]

