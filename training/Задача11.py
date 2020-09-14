a = list(map(int,input().split()))
x = int(input())


check = 0
c = []
for digit in a:
    if digit > x:
        check = digit - x
        c.append(check)
    else:
        check = x - digit
        c.append(check)
link = c.index(min(c))
print(a[link])
