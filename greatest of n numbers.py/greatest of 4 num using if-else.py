#wap to find the greatest of 4 number using if-else statement

num1= int(input('Enter your num1: '))
num2= int(input('Enter your num2: '))
num3= int(input('Enter your num3: '))
num4= int(input('Enter your num4: '))

if (num1 > num2):
    f1 = num1
else:
    f1 = num2

if (num4 > num3):
    f2 = num4
else:
    f2 = num3

if (f1>f2):   
    print(str(f1) + ' is the greatest')
else:
    print(str(f2) + ' is the greatest')
