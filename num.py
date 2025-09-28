#numerical precision in-class assignment

#init

#addition
def add(a1, b1, a2, b2):
    '''
    for two numbers (a1, b1) and (a2, b2), returns (a1, b1) + (a2, b2)
    '''

    if b1 > b2:
        while b1 > b2:
            b1 = b1 - 1
            a1 = 10 * a1
            if b1 = b2:
                break
        a = a1 + a2
        b = b2

    elif b2 > b1:
        while b2 > b1:
            b2 = b2 - 1
            a2 = 10 * a2
            if b2 = b1:
                break
        a = a1 + a2
        b = b1

    elif b1 = b2:
        a = a1 + a2
        b = b1

    return(a, b)

#multiplication
def mult(a1, b1, a2, b2):
    '''
    for two numbers (a1, b1) amd (a2, b2), returns (a1 * a2, b1 + b2)
    '''
    
    a = a1 * a2
    b = b1 + b2
    
    if a == 0:
        return(0, 0)
    
    while a % 10 == 0:
        a3 //= 10
        b += 1
    
    return(a, b)
    
#division

#test

