from firebase import firebase
from firebase_connect import *
from assignment_file import *

funct_type = {'def', 'function'}

def function_checker(line, comment_sym):
    string = line.strip()
    if (string[:3] == comment_sym) or (string[:8] == comment_sym):
        #print(string[:3])
        return True
    return False


def function_count(filename):
    # if is cpp file  
    funct = 0
    if filename[len(filename) - 4:len(filename):1] == '.cpp':
        return 1

    with open(filename, 'r') as infile:
        for line in infile:
            if (len(line) != 1):
                for types in funct_type:
                    if function_checker(line, types):
                        funct = funct + 1
    return funct

for item in file_list:
    count = function_count(file_list[item])
    file_name = file_list[item]
    print(file_list[item], {item: count}, file_name[len(file_name) - 4:len(file_name):1])
    firebase.patch(my_url + '/funct_count', {item: count})