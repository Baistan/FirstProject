numbers = [10,15,20,-5,25,30,40,50,60,-1]

i = 0
j = 0
while i < len(numbers):
    if numbers[i] < 0:
        j += 1
        print("Отрицательный элемент",numbers[i])
    i += 1

print(i,j)