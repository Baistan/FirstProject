text = "hello world its python programmer"
space = text.index(" ")
print(text[:space])


with open("text.txt","w") as f1:
    f1.write(text[:space])