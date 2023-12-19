name = input("Insert file name: ")
n = int(input("Insert an integer: "))

try:
    with open(name, 'r') as file:
        words = []
        while True:
            line = file.readline()
            if not line:
                break
            word = line[:-1]  # Exclude the newline character
            if len(word) > n:
                words.append(word)

        # Sort the words alphabetically using bubble sort
        i = 0
        while i < len(words):
            j = 0
            while j < len(words) - i - 1:
                if words[j] > words[j + 1]:
                    words[j], words[j + 1] = words[j + 1], words[j]
                j += 1
            i += 1
        print(f'The words longer than {n} are the following:')
        for word in words:
            print(word)
except FileNotFoundError:
    print(f'File not found: {name}')