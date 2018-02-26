from firebase import firebase
from firebase_connect import *
from assignment_file import *

def function_checker(line, comment_sym):
    string = line.strip()
    if (string[:3] == comment_sym) or (string[:8] == comment_sym):
        #print(string[:3])
        return True
    return False


def function_count(filename):
    funct = 0
    with open(filename, 'r') as infile:
        for line in infile:
            if (len(line) != 1):
                if function_checker(line, 'def') or function_checker(line, 'function'):
                    funct = funct + 1
    return funct

for item in file_list:
    count = function_count(file_list[item])
    firebase.patch(my_url + '/funct_count', {item: count})