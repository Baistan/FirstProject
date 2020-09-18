str = input()
a = str.replace("A","B")
b = a.replace("C","D")
if "A" and "C" in str:
    print(b)
else:
    print(str)
