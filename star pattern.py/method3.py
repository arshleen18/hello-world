#wap to print the following star pattern:
    *
   ***
  *****
 *******
*********
n = int(input('enter number: '))
for i in range(n):
    print(' '*(n-i-1) + '*'*(2*i+1))
