def division(dividend, divisor):
    sign = (-1 if ((dividend <0) ^ (divisor < 0)) else 1)
    
    dividend = abs(dividend)
    divisor = abs(divisor)
    
    quotient = 0
    tempnum = 0
    
    for i in range(31, -1, -1):
        if (tempnum + (divisor << i) <= dividend):
            tempnum += divisor << i
            quotient |= 1 << i
            
    if sign == -1:
        quotient =-quotient
    return quotient
    
    
a = int(input("Enter dividend : "))
b = int(input("Enter divisor : "))
print("The result is", division(a,b))