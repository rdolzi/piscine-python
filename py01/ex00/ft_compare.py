import sys

if len(sys.argv) != 3:
    print("Please insert two numbers")
else:
    num1 = float(sys.argv[1])
    num2 = float(sys.argv[2])

    if num1 > num2:
        print(str(num1) +" is greater than " +  str(num2))
    if num1 < num2:
        print(str(num1) + " is less than " + str(num2))
    if num1 == num2:
        print(str(num1) + " is equal than " + str(num2))