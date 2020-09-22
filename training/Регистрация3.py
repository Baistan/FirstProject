def registration(username,password,check_password):
    if password == check_password:
        with open("text.txt", "a") as file1:
            file1.write(username)
            file1.write(password)
        return ("Вы успешно зарегистрировались",username,password)
    else:
        return "Данные введены неверно!"

username = input()
password = input()
check_password = input()

def auth(login,passw):
    file1 = open("text.txt")
    check_file = file1.read()
    log = check_file[:len(username)]
    password = check_file[len(username):]
    if login == log and passw == password:
        return "Вы успешно авторизовались"

    return "Вы ввели неверные данные"

login = input()
passw = input()


print(registration(username=username,password=password,check_password=check_password))


print(auth(login=login,passw=passw))