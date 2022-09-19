from leet import leet
from itertools import chain
from tqdm import tqdm


print('''\033[91m 
░█░░░█▀█░▀▀█░█░█░░░█░█░█▀█░█▀▄░█░█░█▀▀░█▀▄░░░█▀█░█▀█░█▀▀░█▀▀░█░█░█▀█░█▀▄░█▀▄
░█░░░█▀█░▄▀░░░█░░░░█▄█░█░█░█▀▄░█▀▄░█▀▀░█▀▄░░░█▀▀░█▀█░▀▀█░▀▀█░█▄█░█░█░█▀▄░█░█
░▀▀▀░▀░▀░▀▀▀░░▀░░░░▀░▀░▀▀▀░▀░▀░▀░▀░▀▀▀░▀░▀░░░▀░░░▀░▀░▀▀▀░▀▀▀░▀░▀░▀▀▀░▀░▀░▀▀░                                                               		 
                     \033[93mBusiness Password Generator\033[93m
''')

name = input('\033[36mBusiness name: ')
if(name == ''):
    print("Error: no business name")
    exit()

years = input('Provide years range [ex: "2000 to 2005" = 2000:2005]: ')
if(years == ''):
    print("Error: no years range")
    exit()
starty = int(years.split(':')[0])
endy = int(years.split(':')[1])
if(endy < starty):
    print("Error: no valid range")
    exit()

morew = str(input("Do you want to enter more words? [y/N]: "))
extrawords = []
if(morew == 'y'):
    words = input("Add words separated with commas [word1,word2,word3,...]: ")
    extrawords = list(chain([name], words.split(',')))
else:
    extrawords = [name]

filename = input('Insert wordlist name: ')

leng = len(extrawords)
passwords = []
for i in range(0, leng):
    passwords = list(chain(passwords, leet(extrawords[i])))

leng = len(passwords)
for i in range(0, leng):
    for j in range(starty, endy):
        passwords.append(passwords[i]+str(j))
    for j in range(0,100):
        passwords.append(passwords[i]+str(j))

f = open(filename, 'w')
for i in tqdm(passwords):
    f.write(str(i)+'\n')