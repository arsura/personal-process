from read_write import *
# word list from https://github.com/dwyl/english-words

# while read word list file
#   if any line have n letter word and n_word list < 100
#       append word to n_word list
# write n_word list to textfile

def read_lines(filename, n_letter, max_word):
    lines = []
    with open(filename, 'r') as infile:
        for line in infile:
            if len(line) == n_letter and len(lines) < max_word:
                lines.append(line)

    return lines

def main():
    n_letter = []

    # 3 + 1 ; 3 is word len, 1 is '\n'
    for i in range(3 + 1, 6 + 1):
        n_letter.append(read_lines("words_alpha_rand.txt", i, 100))
    
    # clear content in text file
    f = open("300_words.txt", 'w+')
    f.truncate()
    f.close()

    for item in n_letter:
        write_lines("300_words.txt", item)

if __name__ == "__main__":
    main()