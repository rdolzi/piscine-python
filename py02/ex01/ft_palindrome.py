import sys



def is_palindrome(str):
    i = 0
    while i < len(str) / 2:
        if str[i] == ' ' or str[len(str) - 1 - i] == ' ':
            i += 1
        elif str[i] != str[len(str) - 1 - i]:
            return "The string "+ str +  " is not palindrome"
        else:
            i += 1
    return "The string "+ str +  " is palindrome"
    

if __name__ == "__main__":
    if len(sys.argv) != 2 :
        print("Error! Insert just 1 string!")
    else:
        print(is_palindrome(str(sys.argv[1])))


# e4r10p2% python -c 'from ft_palindrome import is_palindrome; print(is_palindrome("kayak"))'
# Traceback (most recent call last):
#   File "<string>", line 1, in <module>
#   File "ft_palindrome.py", line 11
#     return f'The string {str} is not palindrome'
#                                                ^
# SyntaxError: invalid syntax
# e4r10p2%