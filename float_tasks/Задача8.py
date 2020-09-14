num = int(input("Введите число:"))
hun = num // 100
cen = num % 100 // 10
numbers = num % 100 % 10
print("Сумма цифр числа", num , "=", hun+cen+numbers)