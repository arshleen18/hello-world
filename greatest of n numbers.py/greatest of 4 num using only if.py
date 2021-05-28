#wap to find greatest of 4 num using only if statement

num1= float(input('Enter your num1: '))
num2= float(input('Enter your num2: '))
num3= float(input('Enter your num3: '))
num4= float(input('Enter your num4: '))

max = num1
if num2 > max:
    max = num2
if num3 > max:
    max = num3
if num4 > max:
    max = num4
print(max)
