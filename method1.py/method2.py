#sum of first n natural numbers

num = int(input('enter that number till which you want the sum: '))
sum = 0
i= 1
while (i <= num):
    sum += i
    i += 1
print('sum: ', sum)
                                   #or
  
n = int(input('enter that number till which you want the sum: '))
sum = (n*(n+1))/2
print('sum of ', n, ' is ', sum ) 
