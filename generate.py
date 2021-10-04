import random

alf = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
       'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
size = len(alf)

with open("names.txt", "w") as file:
    word = []
    for i in range(1000000):
        word = []
        tam = random.randint(3, 12)
        for j in range(tam):
            word.append(alf[random.randint(0, size-1)])
        file.write(''.join(word)+"\n")
