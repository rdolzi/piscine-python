def compute(str1, num1):
    if (len(str1) <= (-num1 if num1 < 0 else num1)):
        return "Error: index out of range"
    return str1[num1] + " " +str1[-num1]

print("Insert a string: ", end="")
str1 = str(input())
num1 = None
while (num1 == None):
    try:
        num1 = int(input("Insert an integer: "))
    except ValueError:
        print("Insert a valid integer!")
        num1 = None
print(compute(str1, num1))
