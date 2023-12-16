import sys 

def is_ordered(lis):
    min = lis[0]
    for l in lis:
        if l > min:
            return 0
        min = l
    return 1 


if len(sys.argv) < 3:
    print("Error! You must insert at least 2 numbers")
else:
    if is_ordered([int(x) for x in sys.argv[1:]]):
        print("The inserted sequence is sorted!")
    else:
        print(f'The correct order is {sorted([int(x) for x in sys.argv[1:]], reverse=True)}')

