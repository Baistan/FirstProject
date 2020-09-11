N = int(input())
a =[]


for i in range(N):
    new_element = int(input())
    a.append(new_element)

maximum_of_a = max(a)
count_of_Max = a.count(maximum_of_a)
print(count_of_Max-1)