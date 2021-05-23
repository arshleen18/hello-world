#wap to check whether a username has more than 10 characters

username = "barshleen@"
if len(username) == 10:
    print('this username has 10 characters')
elif len(username) > 10:
    print('this username has more than 10 characters')
else:
    print('this username has less than 10 characters')
