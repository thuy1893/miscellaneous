
import os
os.chdir("C:\\Users\\nttdo\\learning.python\\miscell")

def backward(word):
    backw = ""
    f = open("output.txt", "w")
    while word:
        loc = len(word)-1
        backw =  backw + word[loc]
        word = word[:loc]
    return f.write(backw)
    f.close()   
word = open("input.txt", "r").read()

print("working...")
backward(word)
print("done. Output saved as text file in ", os.getcwd())


#next step is to read a text file, and convert it to backward text and save it to new text file.