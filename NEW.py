# БИБЛИОТЕКИ


my_dict = dict(Russia = "Moscow",student = ["Erjan","Danil","Baistan","ALina"])
second_dict = {1: "lala",2: "3lalala"}
my_dict["cooler"] = "water"

search = "Russia"


if search in my_dict:
    del my_dict[search]
print(my_dict)
