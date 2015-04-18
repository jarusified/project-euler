sumofsquare=lambda x: x*x

sum=0
sumsquare=0

for i in range(100):
  sumsquare+=i
  sum+=sumofsquare(i)

print sumsquare*sumsquare -sum
