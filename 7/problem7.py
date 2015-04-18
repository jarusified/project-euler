"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?

"""
def prime(n):
  prime=[]
  seive=[True]*(n+1)
  for i in range(2,n+1):
    if seive[i]:
       prime.append(i)
    for j in range(2*i,n+1,i):
      seive[j]=False
  return prime

print prime(1000000)[10001-1]
  
