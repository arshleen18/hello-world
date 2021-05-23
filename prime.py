#to find whether a number is prime or not

num = int(input('enter number: '))
prime = True
for i in range(2, num):
    if (num % i == 0):
        prime = False
        break
if prime:
    print(str(num) + ' ' + 'is prime')
else:
    print(str(num) + ' ' + 'is not prime')
