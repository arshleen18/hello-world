#wap to know whether a student has passed or failed

marks1 = int(input('enter marks\n'))
marks2 = int(input('enter marks\n'))
marks3 = int(input('enter marks\n'))
avg = (marks1 + marks2 + marks3)/3
if (avg >= 40 and marks1 >= 33 and marks2 >= 33 and marks3 >= 33):
    print("you've passed")
else:
    print("you've failed")
