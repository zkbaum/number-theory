#!/usr/bin/env python

# Helper function used in some scripts

def is_prime(n) : 
    """
    Input: Integer n
    Output: Boolean, if n is prime
    Source: https://www.geeksforgeeks.org/python-program-to-check-whether-a-number-is-prime-or-not/
    """
  
    # Corner cases 
    if (n <= 1) : 
        return False
    if (n <= 3) : 
        return True
  
    # This is checked so that we can skip  
    # middle five numbers in below loop 
    if (n % 2 == 0 or n % 3 == 0) : 
        return False
  
    i = 5
    while(i * i <= n) : 
        if (n % i == 0 or n % (i + 2) == 0) : 
            return False
        i = i + 6
  
    return True
