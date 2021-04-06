def encrypt(x, a, b):
    if x == -33:
        return ' '
    else:
        return chr((a*x + b) % 26 + 65)

outputStr = ""
inputString = (input("Input string: "))
a = (int(input("Input a: ")))
b = (int(input("Input b: ")))
list = [(ord(y) - 65) for y in inputString]
output = [encrypt(x, a, b) for x in list]
for i in output:
    outputStr += i
print(outputStr)
