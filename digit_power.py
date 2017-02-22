def numToDigits(a):
    # a is a number, return a as in a list of decimal digits
    a_digits = []
    if a == 0:
        a_digits.append(0)
    else:
        while a >= 1:
            b = a%10
            a_digits.insert(0,b)
            a = (a-b)/10
    return a_digits
    
def digitsToNum(number):
    # a is a list of decimal digits, return a number
    length = len(number)
    num = number[length-1]
    tmp = 10
    for i in range(length-1):
        num += tmp * number[length-i-2]
        tmp *= 10
    return num


def digitsAdd(number1,number2):
    digits1 = numToDigits(number1)
    digits2 = numToDigits(number2)
    flag = True
    if len(digits1) >= len(digits2):
        for i in range(len(digits2)):
            digits1[len(digits1)-len(digits2)+i] += digits2[i]
        while flag:
            status = True
            for i in range(len(digits1)):
                if digits1[i] >= 10:
                    status = False
            if status:
                flag = False
                
            else:
                firstdigit = numToDigits(digits1[0])
                if len(firstdigit) > 1:
                    for i in range(len(firstdigit)-1):
                        digits1.insert(0, firstdigit[len(firstdigit)-i-2])
                    digits1[len(firstdigit)-1] = firstdigit[len(firstdigit)-1]
                    
                for i in range(len(digits1)):
                    if digits1[i] >= 10:                                              
                        tmp = digits1[i]/10  
                        digits1[i] -= tmp*10
                        digits1[i-1] += tmp
        return digitsToNum(digits1)
    else:
        digitsAdd(number2,number1)


 
def digitsMultiply(number1, number2):
    # a and b are both lists of decimal digits corresponding to two numbers
    # return a*b
    value = []
    digits1 = numToDigits(number1)
    digits2 = numToDigits(number2)
    for i in range(len(digits1)):
        tmp = []
        for j in range(len(digits2)):
            tmp.append(int(digits1[i])*int(digits2[j]))
        for k in range(len(digits1)-i-1):
            tmp.append(0)
        value.append(tmp)
    valuesum = digitsToNum(value[0])
    for i in range(len(value)-1):
        valuesum = digitsAdd(valuesum, digitsToNum(value[i+1]))
    return valuesum
                

def power(a,b):
    # list calculation: int only
    a = int(a)
    b = int(b)
    result = a
    for i in range(b-1):
        result = digitsMultiply(result, a)
    return result
    
    
if __name__ == "__main__":
    test = 31231313123
    print "test number:", test
    digit = numToDigits(test)
    print "digit:", digit
    num = digitsToNum(digit)
    print "number:", num
    a = 999
    b = 111
    print "Add:", digitsAdd(a,b)
    print "Multiply:", digitsMultiply(a,b)
    print "Power", power(2,38)
    # print power(2,38)