#!/usr/bin/env python
import math
import sympy
import numpy
import random


DEBUG=False
def print_if_debug(s):
	if DEBUG:
		print(s)
  
# Source: https://www.geeksforgeeks.org/print-all-prime-factors-of-a-given-number/
# A function to returns all prime factors of a given number n 
def primeFactors(n): 
      
    prime_factors = []
    # Print the number of two's that divide n 
    while n % 2 == 0: 
        # print(2)
        prime_factors.append(2)
        n = n / 2
          
    # n must be odd at this point 
    # so a skip of 2 ( i = i + 2) can be used 
    for i in range(3,int(math.sqrt(n))+1,2): 
          
        # while i divides n , print i ad divide n 
        while n % i== 0: 
            # print(i) 
            prime_factors.append(i)
            n = n / i 
              
    # Condition if n is a prime 
    # number greater than 2 
    if n > 2:
        prime_factors.append(n)
        # print(n) 

    return prime_factors

def isCarmichael(n):
	# Uses Korselts Criterion to see if something is a Carmichael number
	if n%2==0:
		print_if_debug("n is even")
		return False
	factors = primeFactors(n)
	print_if_debug("Prime factors of %d are %s" %(n, factors))
	#  Check all p^2 do not divide n
	for p in factors:
		if (n % p**2) == 0:
			print_if_debug("%d^2 DOES divide n=%d" % (p, n))
			return False
		else:
			print_if_debug("%d^2 does NOT divide n=%d" % (p, n))

	# Check all p-1 divide n-1 
	for p in factors:
		if (n-1) % (p-1) == 0:
			print_if_debug("%d-1 does divide %d-1" % (p, n))
		else:
			print_if_debug("%d-1 does NOT divide %d-1" % (p, n))
			return False

	return True
          
def problem_2():
	# FRINT 19.2
	inps = [1105, 1235, 2821, 6601, 8911, 10659, 19747, 105545, 126217, 162401, 172081, 188461]
	# inps = [19747]
	for n in inps:
		print("Investigating if n=%d is a Carmichael number" % n)
		if isCarmichael(n):
			print("Yes! %d is a Carmichael number" % n)
		else:
			print("No. %d is NOT a Carmichael number" % n)
		print("=============")


def problem_3():
	# FRINT 19.3
	found = []
	k=1
	while len(found)<5:
		factors = [6*k+1, 12*k+1, 18*k+1] 
		# make sure all factors are prime
		are_they_prime = [sympy.ntheory.isprime(x) for x in factors]
		if False not in are_they_prime:
			found.append(k)
		k+=1
	print("K's found:",found)
	numbers = []
	for k in found:
		val = (6*k+1) * (12*k+1) * (18*k+1)
		numbers.append(val)
	print("Carmichael Numbers:",numbers)

	"""
	Solution

	K's found: [1, 6, 35, 45, 51]
	Carmichael Numbers: [1729, 294409, 56052361, 118901521, 172947529]
	"""


def problem_4():
	#FRINT 19.5
	n=700000
	while n<900000:
		if isCarmichael(n) and not sympy.ntheory.isprime(n):
			print("Carmichael number:", n)
			print("Factors:",primeFactors(n))
		n+=1

	"""
	Solution

	Carmichael number: 825265
	Factors: [5, 7, 17, 19, 73]
	"""



if __name__=='__main__':
	# problem_2()
	problem_3()
	# problem_4()