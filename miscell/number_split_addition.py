import random
n = random.randint(10,99)
#n = input("input number: ")
def task(n):
    new = []
    for i in str(n):
        new.append(i)
    a = new[0]
    b = new[1]
    return int(a) + int(b)

print(n, "the sum of its digits is: ", task(n))
