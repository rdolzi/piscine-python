def sum_list(list_num):
    sum = 0
    for n in list_num:
        sum += int(n)
    return "The sum is: " + str(sum)


if __name__ == "__main__":
    list_num = []
    while True:
        num = int(input("Insert integer: "))
        if num == 0:
            break
        list_num.append(num)
    print(sum_list(list_num))


