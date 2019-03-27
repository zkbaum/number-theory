#!/usr/bin/env python

# FRINT 14.2
# Calculates the first 10 fermat numbers

def f(x):
	return (2 ** (2**x)) + 1

for i in range(10):
	print("%d\t%d" % (i, f(i)))
