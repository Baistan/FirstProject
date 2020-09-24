s = input()
upper = 0
lower = 0
for i in s:
    if i.isupper():
        upper += 1
    elif i.islower():
        lower += 1
if upper > lower:
    s1 = s.upper()
    print(s1)
elif lower >= upper:
    s2 = s.lower()
    print(s2)

