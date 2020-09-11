
N = list(map(int,input().split()))
sec_num = 0
j = 0
for digit in N:
    if digit > sec_num:
        sec_num = digit
        j = j + 1
print(j-1)


