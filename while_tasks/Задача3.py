num = int(input)
i = 1
result = 0
while result <= num:
    # i += 1       /(i = i + 1)
    result = 2 ** i
    print(i,result)
