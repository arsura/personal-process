def compute_lps(pattern):
    lenght = 0
    i = 1
    M = len(pattern)
    lps = [None] * M
    lps[0] = 0
    while i < M:
        if pattern[i] == pattern[lenght]:
            lenght = lenght + 1
            lps[i] = lenght
            i = i + 1
        else:
            if lenght != 0:
                lenght = lps[lenght - 1]
            else:
                lps[i] = 0
                i = i + 1
    return lps

def kmp_search(pattern, text):
    M = len(pattern)
    N = len(text)
    lps = compute_lps(pattern)
    #print(lps)
    i = 0
    j = 0
    while i < N:
        #print(pattern[j], text[i])
        if pattern[j] == text[i]:
            j = j + 1
            i = i + 1
        if j == M:
            print(i-j)
            j = lps[j - 1]
        elif i < N and pattern[j] != text[i]:
            if  j != 0:
                j = lps[j - 1]
            else:
                i = i + 1

def main():
    text = "siwakorn ruenrit"
    pattern = "enr"
    kmp_search(pattern, text)

if __name__ == "__main__":
    main()


# error log
#   1. else if invalid syntax --> elif
#   2. don't have index 0 at lsp = [] (index out of range) 
