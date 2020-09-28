# import sendgrid
# from sendgrid import Mail
#
# sendgrid_api_key = "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"
# subject = "Registration"
# sg = sendgrid.SendGridAPIClient(sendgrid_api_key)
#
# def send_email(email,code):
#     body = "my code =" + code
#     message = Mail(
#         from_email="maximneveraa@gmail.com",
#         to_emails=email,
#         subject=subject,
#         plain_text_content=body
#     )
#     print(email,code)
#     response = sg.send(message)
#
#
#
#
# def registration(username,password,check_password):
#     global code
#     code = "123456"
#     if password == check_password:
#         print(username,password,check_password)
#         send_email(username,code)
#
#
# registration("emma.apigrid@gmail.com","123456","123456")



strings = ['Samsung j5',
           'samsung galaxy',
           'iphone 10',
           'iphone 5S',
           'samsung a9',
           'ASUS-Roc',
           'Acer HyperX',
           'Macbook Air 18',
           'Macbook Pro 18',
           'geforce gtx460',
           'HDD 1TB',
           'SSD Adata 3100/1400mbs',
           'HDD 2TB',
           'Mac 19',
           'amd Ryzen 490',
           'GeForce TI 2020',
           'SSD Kingston 512 gb',
           'SSD Adata 1TB',
           'Acer zenbook',
           'Asus razer'
           ]





def function1(strings):
    for i in strings:
       with open("LIST.txt","a") as file1:
            file1.write(i.lower() + "\n")\

function1(strings)


def filtration():
    with open("LIST.txt", "r") as file2:
        var = file2.readlines()
        for sentence in var:
            if "samsung" or "iphone" in sentence:
                with open("Phones.txt", "a") as file3:
                    file3.write(sentence)
            elif "acer" in sentence or "asus" in sentence or "macbook" in sentence:
                with open("Computers.txt", "a") as file4:
                    file4.write(sentence)
            elif "geforce" in sentence or "amd" in sentence:
                with open("Videorcarts.txt", "a") as file5:
                    file5.write(sentence)
            elif "hdd" in sentence or "sdd" in sentence:
                with open("HardDrives.txt", "a") as file6:
                    file6.write(sentence)

filtration()



# def open_file(file_name):
#     with open(filename,"r") as file7:
#         var = file7.readlines()
#     return var
#
# print(open_file())
#
# user_input = input()
# if user_input == "phones":
#     open_file("")
# elif:
#     open_file()
