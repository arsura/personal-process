# read data from letter_freq and push to dictionary
# sort dictionary


def read_lines(filename):
    freq_table = {}
    with open(filename, 'r') as infile:
        for line in infile:
            alphabet = line.split(" ")
            freq = alphabet[1].split("\n")
            freq_table[alphabet[0]] = int(freq[0])
    return freq_table

def main():
    freq_table = read_lines("letter_freq.txt")   
    #print(freq_table)

    # sort by value in freq table
    sort_dict = [(k, freq_table[k]) for k in sorted(freq_table, key=freq_table.get, reverse=True)]
    for key, value in sort_dict:
        print(key, "\t", value)

if __name__ == "__main__":
    main()