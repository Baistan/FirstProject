def lineReverse(num):
    global a
    a = []
    while num != 0:
        a.append(num)
        num = int(input())
    a.reverse()
    return a

number = int(input())
print(lineReverse(number))
for integer in a:
    print(integer,end=" ")