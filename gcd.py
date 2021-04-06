def gcd(x,y):
    quotient = 0
    remainder = 0
    if y == 0:
        return x
    else:
        quotient = x//y
        remainder = x%y
        # divideList.append([x,y,quotient,remainder])
        print("{divide} = {divisor} * {quot} + {remain}".format(divide=x, divisor=y, quot=quotient, remain=remainder))
        return gcd(y, remainder)

num1 = int(input("Enter the larger number: "))
num2 = int(input("Enter the smaller number: "))
print("The GCD is: {}".format(gcd(num1, num2)))
