#!/usr/bin/env python

# Solves for f(x) equiv target (mod p)

##### BEGIN: CONFIG #####
DEBUG =  False

def f(x):
	return x**2

p = 5
target = -1

##### END: CONFIG #####

target = target % p
print("Solving the congruence: f(x) equiv %d (mod %d)" % (target, p))

if DEBUG:
	print("i\tf(i)\tf(i) mod p")
	print("---------------------------------")

solutions = []
for i in range(p):
	res = f(i)

	if (res%p)!=target:
		if DEBUG:
			print("%d\t%d\t%d" % (i, res, res%p))
	else:
		solutions.append(i)
		if DEBUG:
			print("%d\t%d\t%d <-- match!" % (i, res, res%p))


print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
if solutions:
	print("Found solutions:", ','.join(str(x) for x in solutions))
else:
	print("No solutions found")