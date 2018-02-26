from firebase import firebase
from firebase_connect import *
from assignment_file import *

def comment_checker(line, comment_sym):
    string = line.strip()
    if (string[:1] == comment_sym):
        return False
    return True

def lines_count(filename):
    lines = 0
    with open(filename, 'r') as infile:
        for line in infile:
            if (len(line) != 1):
                if comment_checker(line, '#') and comment_checker(line, '/'):
                    lines = lines + 1
    return lines

for item in file_list:
    count = lines_count(file_list[item])
    firebase.patch(my_url + '/lines_count', {item: count})