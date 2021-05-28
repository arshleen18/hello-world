#wap to find the greatest of 3 number using def function

def greatest(n1,n2,n3):
    if n1>n2:
        if n1>n3:
            return n1
        
        else:
            return n3

    else:
        if n2>n3:
            return n2
        else:
            return n3

print(greatest(92,9,87))
