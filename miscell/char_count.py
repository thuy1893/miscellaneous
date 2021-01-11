#import pprint
text = "hello world, this is Thuy here"
count = {}
for i in text:
    count.setdefault(i, 0)
    count[i] += 1
print(count)
#next task: take input text file and output to a new text file 