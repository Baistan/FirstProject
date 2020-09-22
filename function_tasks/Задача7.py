def IsPrime(num):

     i = 2
     while num % i != 0:
         i += 1
     if num == i:
         return True
     return False

print(IsPrime(3))
