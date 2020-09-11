numbers = [10,15,20,25,30,40,50,60]
i = 0
max = 0
while i < len(numbers):
    if numbers[i] > max:
       max = numbers[i]
    i += 1
print(max,numbers.index(max))