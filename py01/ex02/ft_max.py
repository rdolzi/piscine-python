import sys


if len(sys.argv) != 4:
    print("Error! Usage: python3 ft_max.py <x> <y> <z>")
else:
    num1 = float(sys.argv[1])
    num2 = float(sys.argv[2])
    num3 = float(sys.argv[3])

    if num1 > num2:
        if num1 > num3:
            macs = num1
        else:
            macs = num3
    else:
        if num2 > num3:
            macs = num2
        else:
            macs = num3
    print( "The max is: " + str(macs))
   