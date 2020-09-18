list1 = list(map(int,input().split()))
num = int(input())

j = 0
if num in list1:
    index_elem = list1.index(num)
    while j < index_elem:
       list1.pop(0)
       j += 1
    print(list1)
elif num not in list1:
    print(list1)

elif len(list1) == 0:
    print(list1)




