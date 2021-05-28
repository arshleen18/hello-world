#wap to find the greatest of 3 numbers using if-else statement

n1=int(input('enter num1: '))
n2=int(input('enter num2: '))
n3=int(input('enter num3: '))

if n1>n2:
        if n1>n3:
            print('greatest number is:', n1) 
        
        else:
            print('greatest number is:', n3)

else:
    if n2>n3:
            print('greatest number is:', n2)
    else:
            print('greatest number is:', n3)
