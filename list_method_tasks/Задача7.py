password = input()
with open("text1.txt","a") as f1:
    f1.write(password + "\n")
if len(password) <= 6:
    print(True)
    with open("text1.txt","a") as f1:
     f1.write("True")
else:
    with open("text1.txt", "a") as f1:
     f1.write("False")
    print(False)

