str = input()
i = 0
a = []
for i in  str:
    a.append(i)

j = 0
while j < len(a):
    if a[j] == "A":
        a[j] = "B"
    elif a[j] == "B":
        a[j] = "A"
    j += 1
for line in a:
    print(line,end="")
