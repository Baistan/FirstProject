def a_n(a,n):
    if n == 1:
        return a
    elif n != 1:
        return a*a_n(a,n-1)

print(a_n(2,5))