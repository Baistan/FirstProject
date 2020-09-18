# number = int(input())
# maximum = 0
# i = 0
# string_number = str(number)
# while i < len(string_number):
#     int_number = int(string_number[i])
#     if int_number > maximum:
#         maximum = int_number
#     i += 1
# print(maximum)

# ИЛИ МОЖНО СДЕЛАТЬ ТАК

number = int(input())
string_number = str(number)
a = []
for i in range(len(string_number)):
    a.append(string_number[i])
print(max(a))