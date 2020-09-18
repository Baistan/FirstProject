string = "We are the best footballplayer in the World"
letter = input()



if letter in string:
    count1 = string.count(letter)
    if count1 == 1:
        print(string.index(letter))
    elif count1 >= 2:
      print(string.find(letter),string.rfind(letter))
else:
    print("NO letter in string")

