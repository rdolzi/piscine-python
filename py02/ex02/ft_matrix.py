import sys

def funz():
    n = 0
    res = []
    while n < int(sys.argv[1]):
        li = []
        m = 0
        while m < int(sys.argv[2]):
            val = float(input(f'Insert the element in position ({n},{m}): '))
            li.append(val)
            m += 1
        res.append(li)
        n += 1

    print("The inserted matrix is:")
    for l in res:
        print(l)

    # SOMMA ROWS 
    n = 0
    sum_row = []
    while n < int(sys.argv[1]):
        sum_r = 0
        m = 0
        while m < int(sys.argv[2]):
            sum_r += res[n][m]
            m += 1
        sum_row.append(sum_r)
        n += 1

    # SOMMA COLUMNS 
    sum_col = []
    m = 0
    while m < int(sys.argv[2]):
        sum_c = 0
        n = 0
        while n < int(sys.argv[1]):
            sum_c += res[n][m]
            n += 1
        sum_col.append(sum_c)
        m += 1

    print("The sum over rows is:")
    print(sum_row)
    print("The sum over columns is:")
    print(sum_col)

if len(sys.argv) != 3:
    print("Error! Usage: python3 ft_matrix.py <n> <m>")
else:
    funz()
