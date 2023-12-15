import sys

if len(sys.argv) <= 2:
    print("Error! Usage: python3 ft_ext_pos.py <x1> ... <xn>")

i = 1
max = int(sys.argv[1])
max_pos = 0
min = int(sys.argv[1])
min_pos = 0
while i < len(sys.argv) - 1:
    if int(sys.argv[i]) > max:
        max = int(sys.argv[i])
        max_pos = i - 1
    if int(sys.argv[i]) < min:
        min = int(sys.argv[i])
        min_pos = i - 1
    i += 1

print(f'The min is {min} and its position is {min_pos}')
print(f'The max is {max} and its position is {max_pos}')

