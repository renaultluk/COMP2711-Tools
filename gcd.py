divideList = []

def gcd(x,y):
    quotient = 0
    remainder = 0
    if y == 0:
        return x
    else:
        quotient = x//y
        remainder = x%y
        divideList.append([x,y,quotient,remainder])
        print("{divide} = {divisor} * {quot} + {remain}".format(divide=x, divisor=y, quot=quotient, remain=remainder))
        return gcd(y, remainder)

def bezout():
    print("Rewriting: ")
    for i in divideList:
        print("{remain} = {divide} - {divisor} * {quot}".format(remain=i[3], divide=i[0], divisor=i[1], quot=i[2]))
     
    count = len(divideList) - 2
    while count != 0:
        

num1 = int(input("Enter the larger number: "))
num2 = int(input("Enter the smaller number: "))
print("The GCD is: {}".format(gcd(num1, num2)))
bezout()
