str = input("Insert a string:")
len_s = len(str)

if len_s > 20:
    print(str[-20:])
else:
        print('X' * (20 - len_s) + str)
