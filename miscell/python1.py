#import os
#print(os.getcwd())
#os.chdir('C:\Users\nttdo\Downloads') i forgot the \\

import os
os.chdir("C:\\Users\\nttdo\\learning.python\\miscell")

def backward(word):
    backw = ""
    while word:
        loc = len(word)-1
        backw += word[loc]
        word = word[:loc]
    return backw

word = input("input here the word you want to see spelt backward: ")
print('\n',backward(word))
#next step is to create a random text of ATCG, and write a new text file with the complementary bases (replace A with T, T with A, G with C and C with C, and write in backward)
