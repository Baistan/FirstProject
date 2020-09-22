def file_work(string):
    if string == "read":
        with open("test.txt","r") as f1:
            return f1.read()
    elif string == "write":
        with open("test.txt","w") as f1:
            new_file = input()
            return f1.write(new_file)

str = input()
print(file_work(str))

