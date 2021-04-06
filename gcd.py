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
        for i in range(count):
            for j in range(4):
                if divideList[i][3] == divideList[count][j]:
                    divideList[count][j] = "({divide} - {divisor} * {quot})".format(divide=divideList[i][0], divisor=divideList[i][1], quot=divideList[i][2])
                    print("{remain} = {divide} - {divisor} * {quot}".format(remain=divideList[i][3], divide=divideList[i][0], divisor=divideList[i][1], quot=divideList[i][2]))


num1 = int(input("Enter the larger number: "))
num2 = int(input("Enter the smaller number: "))
print("The GCD is: {}".format(gcd(num1, num2)))
bezout()
