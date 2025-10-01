#numerical precision in-class assignment

#init

class HPNumber:
    """
    Hige-precision number represented as (a, b) meaning a * 10^b
    """
    def __init__(self, a: int, b: int):
        self.a, self.b = self.remove_trailing_zeros(a, b)

    def __repr__(self):
        return f"({self.a}, {self.b})"
    
    def __str__(self):
        return f"{self.a}e{self.b}"

    #addition
    def __add__(self, other):
        '''
        for two numbers (a1, b1) and (a2, b2), returns (a1, b1) + (a2, b2)
        '''

        a1, b1 = self.a, self.b
        a2, b2 = other.a, other.b

        if b1 > b2:
            while b1 > b2:
                b1 = b1 - 1
                a1 = 10 * a1
                if b1 == b2:
                    break
            a = a1 + a2
            b = b2

        elif b2 > b1:
            while b2 > b1:
                b2 = b2 - 1
                a2 = 10 * a2
                if b2 == b1:
                    break
            a = a1 + a2
            b = b1

        elif b1 == b2:
            a = a1 + a2
            b = b1

        return HPNumber(*self.remove_trailing_zeros(a, b))
        
    #subtraction
    def __sub__(self, other):
        '''
        for two numbers (a1, b1) and (a2, b2), returns (a1, b1) - (a2, b2)
        '''

        a1, b1 = self.a, self.b
        a2, b2 = -1*other.a, other.b

        return HPNumber(a1, b1) + HPNumber(a2, b2)

    #multiplication
    def __mul__(self, other):
        '''
        for two numbers (a1, b1) amd (a2, b2), returns (a1 * a2, b1 + b2)
        '''
        
        a = self.a * other.a
        b = self.b + other.b
        
        if a == 0:
            return HPNumber(0, 0)
        
        while a % 10 == 0:
            a //= 10
            b += 1
        
        return HPNumber(*self.remove_trailing_zeros(a, b))
        
    #division
    def __truediv__(self, other, prec=20):
        '''
        For two numbers (a1,b1) and (a2,b2), returns the quotient (a1/a2, b1-b2)
        '''
        if other.a == 0:
            raise ZeroDivisionError
        if self.a == 0:
            return HPNumber(0,0)
        
        a1, b1 = self.a, self.b
        a2, b2 = other.a, other.b
        sign_1 = 1-2*(a1<0)
        sign_2 = 1-2*(a2<0)
        a1 *= sign_1
        a2 *= sign_2
        
        num_digits_1 = len(str(a1))
        num_digits_2 = len(str(a2))
        exponent = max(num_digits_2 - num_digits_1, 0) + max(prec, 1)
        
        quotient = self.long_division(a1*10**(exponent), a2)
        
        return HPNumber(*self.remove_trailing_zeros(quotient*sign_1*sign_2, b1-b2-exponent))
    
    def __lt__(self, other):
        '''
        Check if self < other
        '''
        return not (self-other).is_positive()
        
    def __le__(self, other):
        '''
        Check if self <= other
        '''
        subtraction = self-other
        return not subtraction.is_positive() or subtraction.a==0
    
    def __gt__(self, other):
        '''
        Check if self > other
        '''
        subtraction = self-other
        return (self-other).is_positive()
    
    def __ge__(self, other):
        '''
        Check if self >= other
        '''
        subtraction = self-other
        return (self-other).is_positive() or subtraction.a==0
    
    def __eq__(self, other):
        '''
        Check if self == other
        '''
        return (self-other).a == 0
    
    def __ne__(self, other):
        '''
        Check if self != other
        '''
        return (self-other).a != 0
        
    def is_positive(self):
        '''
        Check if a high precision number is positive
        '''
        return self.a>0
    
    def floatlike_string(self):
        '''
        Get a string which is easier to visually compare to a float
        '''
        a_string = str(self.a)
        if len(a_string)==1:
            return self.__str__()
        
        exponent = self.b+len(a_string)-1
        coefficient = a_string[0]+"."+a_string[1:]
        return coefficient+"e"+str(exponent)
        
            
    @staticmethod
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
        
    @staticmethod
    def remove_trailing_zeros(a, b):
        '''
        Remove trailing zeroes from the coefficient a while keeping the number (a,b) the same.
        '''
        if a==0:
            return (0,0)
        coefficient_string = str(a)
        exponent = b
        while int(coefficient_string[-1])==0:
            coefficient_string = coefficient_string[:-1]
            exponent += 1
        return (int(coefficient_string), exponent)
    #test
