numbers = [10,15,20,-5,-5,25,30,40,50,60,-1]

i = 0

while i < len(numbers):
    sec_num = numbers[i]
    i += 1
    if numbers[i] > 0 and sec_num > 0:
         print(numbers[i],sec_num)
    elif numbers[i] < 0 and sec_num < 0:
         print(numbers[i], sec_num)


