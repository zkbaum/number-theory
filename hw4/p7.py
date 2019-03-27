#!/usr/bin/env python

# FRINT 21.3
# This script helps in reducing a bunch of things mod m


QR = [11,13,23,37,47,59,61,71,73,83,97,107,109]
NR = [5,7,17,19,29,31,41,43,53,67,79,89,101,103,113,127]


# Reduce modulo i for a bunch of i's...eventually, we get some
# good info for i=12
for i in range(3,15):
    QR_reduced = [ x%i for x in QR]
    NR_reduced = [ x%i for x in NR]
    print("QR mod %d: %s" %(i, QR_reduced))
    print("NR mod %d: %s" %(i, NR_reduced))
    print("-------")