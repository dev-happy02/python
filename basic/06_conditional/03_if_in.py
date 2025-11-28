p1 = "money"
p2 = "buy now"
p3 = "click"
p4 = "offer"


massage = input("enter your comment : ")

if ((p1 in massage) or (p2 in massage) or (p3 in massage) or (p4 in massage)):
    print("this massage is spam")

else:
    print("this is not a spam massage")
