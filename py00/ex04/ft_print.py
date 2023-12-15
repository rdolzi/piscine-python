def compute(str1, num1):
    if (len(str1) <= (-num1 if num1 < 0 else num1)):
        print("Error: index out of range", end="")
        return 0
    return 1

print("Insert a string: ", end="")
str1 = str(input())
num1 = None
while num1 == None:
    try:
        num1 = int(input("Insert an integer: "))
    except ValueError:
        print("Insert a valid integer!", end="")
        num1 = None
if compute(str1, num1):
    if num1 < 0:
        print(str1[num1:-num1])
    else:
        print(str1[num1:-num1 + len(str1) + 1])

