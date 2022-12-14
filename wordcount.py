import sys

"""Count words in file."""

def word_count(input_file):

    input_file = open(input_file)

    my_dict = {}


    for line in input_file:

        line = line.rstrip()

        words = line.split()

        for word in words:
            my_dict[word] = my_dict.get(word, 0) + 1


    for word, count in my_dict.items():
        print(word, count)

word_count('test.txt')
word_count('twain.txt')

input_file = sys.argv[1]
