x = int(input())
y = int(input())

result = x
i = 1


while result <= y:
    result = result + result * 0.1
    i+=1
print(i)
