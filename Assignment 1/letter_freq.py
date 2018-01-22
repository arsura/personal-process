# alphabet_list = []                                    // [0] = a, [25] = z
# while read 300 word lists file
#   for line in 300 word lists
#       for character in line
#           if character >= 65 and character <= 90      // A - Z (Upper Case)
#               character = character + 32              // Convert to a - z (Lower Case) 
#           alphabet_list[character - 97] += 1 

def read_and_count_single(filename):
    single_alphabet = []

    # fill single_alphabet with 0
    for i in range(26):
        single_alphabet.append(0)

    with open(filename, 'r') as infile:
        for line in infile:
            line.lower()
            for character in line:
                if character >= 'a' and character <= 'z':
                    single_alphabet[ord(character) - 97] += 1
    return single_alphabet


def read_and_count_double(filename):
    double_alphabet = []

    for i in range(26):
        double_alphabet.append([])
        for j in range(26):
            double_alphabet[i].append(0)

    with open(filename, 'r') as infile:
        for line in infile:
            line.lower()
            for i in range(0, (len(line) - 2)):
                if line[i] >= 'a' and line[i] <= 'z':
                    double_alphabet[ord(line[i]) - 97][ord(line[i + 1]) - 97] += 1
    return double_alphabet

def write_lines(filename, word):
    outfile = open(filename, 'a')
    outfile.write("".join(word))
    outfile.close()

def clear_content(filename):
    f = open(filename, 'w+')
    f.truncate()
    f.close()

def main():
    # clear text in letter_freq.txt
    clear_content("letter_freq.txt")

    single_alphabet = read_and_count_single("300_words.txt")
    # print freq of single alphabet
    i = 0
    for char in range(ord('a'), ord('z') + 1):
        printout = chr(char) + " " + str(single_alphabet[i]) + "\n"
        #print(printout)
        write_lines("letter_freq.txt", printout)
        i += 1

    double_alphabet = read_and_count_double("300_words.txt")
    # print freq of double alphabet
    i = 0
    j = 0
    for first in range(ord('a'), ord('z') + 1):
        j = 0
        for sec in range(ord('a'), ord('z') + 1):
            printout = chr(first) + chr(sec) + " " + str(double_alphabet[i][j]) + "\n"
            #print(printout)
            write_lines("letter_freq.txt", printout)
            j += 1 
        i += 1
    
if __name__ == "__main__":
    main()