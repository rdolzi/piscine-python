import pickle

if __name__ == "__main__":
    word_length_count = {}

    with open('words.txt', 'r') as file:
        for line in file:
            word_length = len(line[:-1])
            # Update the dictionary with the word length count
            # It checks if the word_length is already a key in the dictionary. If it is, it increments the corresponding value by 1. If it's not, it adds a new key-value pair with the word_length as the key and 1 as the initial value.
            word_length_count[word_length] = word_length_count.get(word_length, 0) + 1

    with open('word_count.pickle', 'wb') as pickle_file:
        pickle.dump(word_length_count, pickle_file)
