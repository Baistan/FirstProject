# a = list(map(int,input().split()))
# max = 1
# i = 0
# while i < len(a):
#     if a[i] > max:
#         max = a[i]
#     i += 1
# j = 0
# check = 0
# check1 = 0
# b = []
# while j < len(a):
#     check = max - a[j]
#     j = j + 1
#     b.append(check)
# x = 0
# maximum_of_check = 0
# while x < len(b):
#     if b[x] >= maximum_of_check:
#         maximum_of_check = b[x]
#     x = x + 1
# link1 = b.index(maximum_of_check)
# link2 = a[link1]
# print(link2)


# ИЛИ МОЖНО ПРОСТО ВОТ ТАК

a = list(map(int,input().split()))
print(min(a))