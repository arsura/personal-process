import random

def read_lines(filename):
    lines = []
    with open(filename, 'r') as infile:
        for line in infile:
            lines.append(line)
    return lines

def write_lines(filename, word):
    outfile = open(filename, 'a')
    outfile.write("".join(word))
    outfile.close()

def clear_content(filename):
    f = open(filename, 'w+')
    f.truncate()
    f.close()

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