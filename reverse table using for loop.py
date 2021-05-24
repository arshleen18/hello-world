#wap to print table of a number in reversed order

n = int(input('enter number: '))
for i in range(10,0,-1):
    b=n*i
    print(f"{n} X {i} = {b}")
