#!/usr/bin/env python
import sympy

# Sees if any prime numbers can be not +/- 1 modulo 6
def is_quadratic_residue(a, p):
	# Checks if a is a quadratic residue modulo p
	# Source: http://pythonfiddle.com/quadratic-residue-detector/
	halfway_point = int((p-1)/2)
	for b in range(0,halfway_point+1):
	    if (b ** 2) % p == a:
	        return True
	return False

primes = list(sympy.primerange(6, 100))
a = 5
QR_for = []
NR_for = [] 
for p in primes:
	if is_quadratic_residue(a,p):
		QR_for.append(p)
	else:
		NR_for.append(p)
		

print("{} is a QR mod {}".format(a, QR_for))
print("{} is a NR mod {}".format(a, NR_for))
print("***********")

for i in range(3, 7):
	reduced = [x%i for x in QR_for]
	print("Reducing QR mod %d gives us:" %i,  reduced)
	reduced = [x%i for x in NR_for]
	print("Reducing NR mod %d gives us:" %i,  reduced)
	print("--------")
# print("{} is a NR mod {}".format(a, NR_for))