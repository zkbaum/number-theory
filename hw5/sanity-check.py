#!/usr/bin/env python
import sympy

# Sees if any prime numbers can be not +/- 1 modulo 6
primes = list(sympy.primerange(4, 500))
dic = {}
for p in primes:
	val = p%6
	if val not in dic:
		dic[val] = 0
	dic[val]+=1
print(dic)
