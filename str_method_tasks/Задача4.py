string = input()
if string[0].islower() and len(string) < 10:
    print(string[0].islower())
    string = string.upper()
    print(string)
elif string[0].isupper() and len(string) < 10:
    print(string[0].isupper())
    string = string.lower()
    print(string)
elif len(string) > 10:
    print(len(string))
    string = string.capitalize()
    print(string)