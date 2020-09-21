s = input()

if len(s) == 11 and s[0:2] == "+7":
    print(s)
elif len(s) == 10:
    print("+7" + s[1:])
elif len(s) == 9:
    print("+7" + s)
