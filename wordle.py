import codecs
import random
with codecs.open("wordle1.txt", 'r', encoding='utf-8',
                 errors='ignore') as f:
    data = f.read()
    five = data.split()
word = random.choice(five)
a = True
count = 0
while(a == True):
    i = input("try ")
    if len(i) != 5:
        continue
    if i not in five:
        print("not in list")
        continue
    if i == word:
        print(word + " is true")
        a = False
    elif i != word and count == 5:
        print(word)
        a = False
    else:
        for j in range(5):
            if i[j] == word[j]:
                print(i[j]+" green")
            elif i[j] in word:
                print(i[j] + " yellow")
            else:
                print(i[j] + " gray")
        count += 1