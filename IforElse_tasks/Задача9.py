n = int(input("Введите длину"))
m = int(input("Введите ширину"))
k = int(input("Введите количество требуемых долек"))

summ = n*m
if (summ - k) % n == 0 or (summ - k) % n == 0:
    print("YES")
else:
    print("NO")