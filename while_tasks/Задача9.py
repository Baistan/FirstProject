i = 1
max = 0

num = int(input())
while num != 0:
   if num > max:
      max = num
   num = int(input())
   if num == max:
      i += 1

print(i)