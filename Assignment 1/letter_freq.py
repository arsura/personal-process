# alphabet_list = []                                    // [0] = a, [25] = z
# while read 300 word lists file
#   for line in 300 word lists
#       for character in line
#           if character >= 65 and character <= 90      // A - Z (Upper Case)
#               character = character + 32              // Convert to a - z (Lower Case) 
#           alphabet_list[character - 97] += 1             
#


def read_and_count_single(filename):
    single_alphabet = []

    # fill single_alphabet with 0
    for i in range(26):
        single_alphabet.append(0)

    with open(filename, 'r') as infile:
        for line in infile:
            line.lower()
            #print(line)
            for character in line:
                if character >= 'a' and character <= 'z':
                    single_alphabet[ord(character) - 97] += 1
                    #print(ord(character))
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
            #print(line)
            for i in range(0, (len(line) - 2)):
                if line[i] >= 'a' and line[i] <= 'z':
                    double_alphabet[ord(line[i]) - 97][ord(line[i + 1]) - 97] += 1
                    #print(ord(line[i]) - 97, "\t", ord(line[i + 1]) - 97)
    return double_alphabet


def main():
    single_alphabet = read_and_count_single("300_words.txt")
    # print freq of single alphabet
    i = 0
    for char in range(ord('a'), ord('z') + 1):
        print(chr(char), " ", single_alphabet[i])
        i += 1

    double_alphabet = read_and_count_double("300_words.txt")
    # print freq of double alphabet
    i = 0
    j = 0
    for first in range(ord('a'), ord('z') + 1):
        j = 0
        for sec in range(ord('a'), ord('z') + 1):
            print(chr(first) + chr(sec), " ", double_alphabet[i][j])
            j += 1 
        i += 1
    
    

if __name__ == "__main__":
    main()