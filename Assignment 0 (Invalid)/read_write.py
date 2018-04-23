def write_lines(filename, word):
    outfile = open(filename, 'a')
    outfile.write("".join(word))
    outfile.close()

def clear_content(filename):
    f = open(filename, 'w+')
    f.truncate()
    f.close()
