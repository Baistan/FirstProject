num = int(input())
summary = 0
i = 0

while num != 0:
    summary = summary + num
    i = i + 1
    num = int(input())
print(i, summary,"Среднее арифметическое: ",summary/i)
