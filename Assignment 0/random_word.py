import random
from read_write import *

def read_lines(filename):
    lines = []
    with open(filename, 'r') as infile:
        for line in infile:
            lines.append(line)
    return lines

def random_lines():
    rand_line = []
    word_list = read_lines('words_alpha.txt')

    for i in range(len(word_list)):
        word_size = len(word_list)
        rand_int = random.randrange(word_size)

        current_word = word_list[rand_int]
        word_list.pop(rand_int)
        rand_line.append(current_word)
    #print(current_word, rand_int)
    clear_content('words_alpha_rand.txt')
    write_lines('words_alpha_rand.txt', rand_line)


def main():
    random_lines()



main()

# random
#print(random.randrange(9))