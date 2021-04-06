def encrypt(p, n, e):
    return p**e % n

outputStr = ""
inputString = (input("Input string: "))
n = (int(input("Input n: ")))
e = (int(input("Input e: ")))
list = [(ord(y) - 65) for y in inputString]
output = [encrypt(x, n, e) for x in list]
# for i in output:
#     outputStr += i
print(output)