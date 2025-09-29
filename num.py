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
def div(a1, b1, a2, b2):
    '''
    For two numbers (a1,b1) and (a2,b2), returns the quotient (a1/a2, b1-b2)
    '''
    if a2==0:
        raise ZeroDivisionError
    if a1==0:
        return (0,0)
    
    sign_1 = 1-2*(a1<0)
    sign_2 = 1-2*(a2<0)
    a1 *= sign_1
    a2 *= sign_2
    
    num_digits_1 = len(str(a1))
    num_digits_2 = len(str(a2))
    exponent = max(num_digits_2 - num_digits_1, 0) + 20
    
    quotient = long_division(a1*10**(exponent), a2)
    
    return (quotient*sign_1*sign_2, b1-b2-exponent)
    
def long_division(dividend, divisor):
    '''
    Compute dividend/divisor using long division, discarding the remainder
    '''
    dividend_string = str(dividend)
    remainder = 0
    quotient = ""
    num_dividend_digits = 1
    
    for i in range(len(dividend_string)):
        quotient_digit = 0
        dividend_chunk = dividend_string[:num_dividend_digits]
        if divisor <= int(dividend_chunk):
            while (quotient_digit + 1) * divisor <= int(dividend_chunk):
                quotient_digit += 1
            remainder = int(dividend_chunk) - (quotient_digit * divisor)
            dividend_string = str(remainder) + dividend_string[num_dividend_digits:]
            num_dividend_digits = len(str(remainder))+1
        else:
            num_dividend_digits += 1
        quotient += str(quotient_digit)
    return int(quotient)
#test

