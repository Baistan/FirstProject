x = int(input())
y = int(input())
z = int(input())

if x == y and y == z:
    print(3)
elif x == y or y == z or z == x:
    print(2)
else:
    print(0)
