def multiply(n1,n2):
    if not n2:
        return 0
    if n2 > 0:
        return n1 + multiply(n1, n2-1)
    else:
        return -1 * n1 + multiply(n1, n2+1)

def tailMultiply(n1,n2, psum =0):
    if not n2:
        return psum
    if n2 > 0:
        return tailMultiply(n1, n2-1, psum + n1)
    else:
        return tailMultiply(n1, n2+1, psum + (-1 * n1))


def loopMultiply(n1,n2):
    psum = 0
    if n2:
        sign = n2//abs(n2)
    else:
        return 0
    for i in range(abs(n2)):
        psum += n1
    return psum * sign

print(loopMultiply(0, -1))

def Add(x, y): 
    # Iterate till there is no carry  
    while (y != 0): 
      
        # carry now contains common 
        # set bits of x and y 
        carry = x & y 
        print(carry,x,y)
  
        # Sum of bits of x and y where at 
        # least one of the bits is not set 
        x = x ^ y 
        print(carry,x,y)

  
        # Carry is shifted by one so that    
        # adding it to x gives the required sum 
        y = carry << 1
        print(carry,x,y)

      
    return x 
  
print(Add(9, 2)) 
