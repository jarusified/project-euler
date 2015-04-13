"""
Problem 1:
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

target=999

def sumdivisible(n):
	p=target/n
	return (n*p*(p+1))/2

print sumdivisible(3)+sumdivisible(5)-sumdivisible(15)