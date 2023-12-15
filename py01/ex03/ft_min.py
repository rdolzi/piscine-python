import sys

def my_min(num1=0, num2=0,num3=0):
    if num1 < num2:
        if num1 < num3:
            macs = num1
        else:
            macs = num3
    else:
        if num2 < num3:
            macs = num2
        else:
            macs = num3
    return macs

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Error! Usage: python3 ft_min.py <x> <y> <z>")
    else:
        num1 = float(sys.argv[1])
        num2 = float(sys.argv[2])
        num3 = float(sys.argv[3])
        print( "The min is: " + str(my_min(num1,num2,num3)))

   