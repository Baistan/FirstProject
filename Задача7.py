num = int(input())
check = []

original_cart = list(range(1,num+1))
original_cart_sum = sum(original_cart)

for i in range(1,num):
    new = int(input())
    check.append(new)

search_cart = original_cart_sum - sum(check)

print("ПОтерялась картояка под номером: ",search_cart)

