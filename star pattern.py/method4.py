#wap to print the following star pattern:
 *********
  *******
   *****
    ***
     *

n = int(input('enter number: '))
for i in range(n,0,-1):
    print(' '*(n-i+1) + '*'*(2*i-1))
