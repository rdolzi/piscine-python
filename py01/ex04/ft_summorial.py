import sys


if len(sys.argv) != 2:
    print("Error! Usage: python3 ft_summorial.py <n>")
else:
    num = int(sys.argv[1])
    if num < 0:
        print("Error! n must be >=0")
    else:
        sum41= 0
        while num > 0:
            sum41 += num
            num -= 1
        print("The sum is: " + str(sum41))
    