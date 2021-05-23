#wap to check whether a message is spam or not

text = input("Enter the text\n")
if("make a lot of money" in text):
    spam = True
elif("buy now" in text):
   spam = True
else:
    spam = False

if (spam):
    print("This text is spam")
else:
    print("This text is not spam")
