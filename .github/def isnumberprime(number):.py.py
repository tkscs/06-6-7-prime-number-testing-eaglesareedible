n = 1000000000000066600000000000001
prime = True
for i in range(2, n):
  print(i)
  if n % i ==0:
    prime = False
    if prime ==False:
      break
if prime:
  print('The number is prime')
else:
  print('The number is not prime')