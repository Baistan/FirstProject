num = int(input())
maximum = 0
while num != 0:
    if num > maximum:
        maximum = num
        print(maximum)
    num = int(input())
print(maximum)