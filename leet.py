from itertools import combinations

def replace(word, index, char):
    if(type(index)==int):
        return word[:index]+char+word[index+1:]
    elif(type(index)==list):
        defword = word
        for i in range(0, len(index)):
            ind = index[i] 
            defword=defword[:ind]+char+defword[ind+1:]
        return defword
    else:
        print("Error de replace, tipo de dato no reconocido: "+str(type(index)))

def leet(word):
    wordlist = []
    tempwordlist = []
    wordlist.append(word)
    changes = -1
    wordlistindex = 0
    while(changes != 0):       
        if(wordlistindex>len(wordlist)):
            pass
        word = wordlist[wordlistindex]
        changes = 0
        #Sustituciones de 'a' por '@'
        letter = 'a'
        sust = '@'
        i = word.find(letter)
        find = []
        while(i!=-1):
            find.append(i)
            i = word.find(letter,i+1)
        i = word.find(letter.upper())
        while(i!=-1):
            find.append(i)
            i = word.find(letter,i+1)
        combt = []
        for i in range(1, len(find)+1):
            comb=combinations(find, i)
            for j in list(comb):
                combt.append(j)
        for i in combt:
            tempwordlist.append(replace(word, list(i), letter))
            tempwordlist.append(replace(word, list(i), letter.upper()))
            tempwordlist.append(replace(word, list(i), sust))
        for i in tempwordlist:
            if i not in wordlist:
                changes+=1
                wordlist.append(i)

        #Sustituciones de 'e' por '3'
        letter = 'e'
        sust = '3'
        i = word.find(letter)
        find = []
        while(i!=-1):
            find.append(i)
            i = word.find(letter,i+1)
        i = word.find(letter.upper())
        while(i!=-1):
            find.append(i)
            i = word.find(letter,i+1)
        combt = []
        for i in range(1, len(find)+1):
            comb=combinations(find, i)
            for j in list(comb):
                combt.append(j)
        for i in combt:
            tempwordlist.append(replace(word, list(i), letter))
            tempwordlist.append(replace(word, list(i), letter.upper()))
            tempwordlist.append(replace(word, list(i), sust))
        for i in tempwordlist:
            if i not in wordlist:
                changes+=1
                wordlist.append(i)

        #Sustituciones de 'i' por '1'
        letter = 'i'
        sust = '1'
        i = word.find(letter)
        find = []
        while(i!=-1):
            find.append(i)
            i = word.find(letter,i+1)
        i = word.find(letter.upper())
        while(i!=-1):
            find.append(i)
            i = word.find(letter,i+1)
        combt = []
        for i in range(1, len(find)+1):
            comb=combinations(find, i)
            for j in list(comb):
                combt.append(j)
        for i in combt:
            tempwordlist.append(replace(word, list(i), letter))
            tempwordlist.append(replace(word, list(i), letter.upper()))
            tempwordlist.append(replace(word, list(i), sust))
        for i in tempwordlist:
            if i not in wordlist:
                changes+=1
                wordlist.append(i)
        
        #Sustituciones de 'o' por '0'
        letter = 'o'
        sust = '0'
        i = word.find(letter)
        find = []
        while(i!=-1):
            find.append(i)
            i = word.find(letter,i+1)
        i = word.find(letter.upper())
        while(i!=-1):
            find.append(i)
            i = word.find(letter,i+1)
        combt = []
        for i in range(1, len(find)+1):
            comb=combinations(find, i)
            for j in list(comb):
                combt.append(j)
        for i in combt:
            tempwordlist.append(replace(word, list(i), letter))
            tempwordlist.append(replace(word, list(i), letter.upper()))
            tempwordlist.append(replace(word, list(i), sust))
        for i in tempwordlist:
            if i not in wordlist:
                changes+=1
                wordlist.append(i)

        #Sustituciones de 's' por '5'
        letter = 's'
        sust = '5'
        i = word.find(letter)
        find = []
        while(i!=-1):
            find.append(i)
            i = word.find(letter,i+1)
        i = word.find(letter.upper())
        while(i!=-1):
            find.append(i)
            i = word.find(letter,i+1)
        combt = []
        for i in range(1, len(find)+1):
            comb=combinations(find, i)
            for j in list(comb):
                combt.append(j)
        for i in combt:
            tempwordlist.append(replace(word, list(i), letter))
            tempwordlist.append(replace(word, list(i), letter.upper()))
            tempwordlist.append(replace(word, list(i), sust))
        for i in tempwordlist:
            if i not in wordlist:
                changes+=1
                wordlist.append(i)
        
        #Sustituciones de 't' por '7'
        letter = 't'
        sust = '7'
        i = word.find(letter)
        find = []
        while(i!=-1):
            find.append(i)
            i = word.find(letter,i+1)
        i = word.find(letter.upper())
        while(i!=-1):
            find.append(i)
            i = word.find(letter,i+1)
        combt = []
        for i in range(1, len(find)+1):
            comb=combinations(find, i)
            for j in list(comb):
                combt.append(j)
        for i in combt:
            tempwordlist.append(replace(word, list(i), letter))
            tempwordlist.append(replace(word, list(i), letter.upper()))
            tempwordlist.append(replace(word, list(i), sust))
        for i in tempwordlist:
            if i not in wordlist:
                changes+=1
                wordlist.append(i)
        
        #Sustituciones de 'g' por '6'
        letter = 'g'
        sust = '6'
        i = word.find(letter)
        find = []
        while(i!=-1):
            find.append(i)
            i = word.find(letter,i+1)
        i = word.find(letter.upper())
        while(i!=-1):
            find.append(i)
            i = word.find(letter,i+1)
        combt = []
        for i in range(1, len(find)+1):
            comb=combinations(find, i)
            for j in list(comb):
                combt.append(j)
        for i in combt:
            tempwordlist.append(replace(word, list(i), letter))
            tempwordlist.append(replace(word, list(i), letter.upper()))
            tempwordlist.append(replace(word, list(i), sust))
        for i in tempwordlist:
            if i not in wordlist:
                changes+=1
                wordlist.append(i)

        #Sustituciones de 'l' por '1'
        letter = 'l'
        sust = '1'
        i = word.find(letter)
        find = []
        while(i!=-1):
            find.append(i)
            i = word.find(letter,i+1)
        i = word.find(letter.upper())
        while(i!=-1):
            find.append(i)
            i = word.find(letter,i+1)
        combt = []
        for i in range(1, len(find)+1):
            comb=combinations(find, i)
            for j in list(comb):
                combt.append(j)
        for i in combt:
            tempwordlist.append(replace(word, list(i), letter))
            tempwordlist.append(replace(word, list(i), letter.upper()))
            tempwordlist.append(replace(word, list(i), sust))
        for i in tempwordlist:
            if i not in wordlist:
                changes+=1
                wordlist.append(i)
        #Sustituciones de 'ñ' por 'n'
        letter = 'ñ'
        sust = 'n'
        i = word.find(letter)
        find = []
        while(i!=-1):
            find.append(i)
            i = word.find(letter,i+1)
        i = word.find(letter.upper())
        while(i!=-1):
            find.append(i)
            i = word.find(letter,i+1)
        combt = []
        for i in range(1, len(find)+1):
            comb=combinations(find, i)
            for j in list(comb):
                combt.append(j)
        for i in combt:
            tempwordlist.append(replace(word, list(i), letter))
            tempwordlist.append(replace(word, list(i), letter.upper()))
            tempwordlist.append(replace(word, list(i), sust))
        for i in tempwordlist:
            if i not in wordlist:
                changes+=1
                wordlist.append(i)

        #Sustituciones de 'ñ' por 'N'
        letter = 'ñ'
        sust = 'N'
        i = word.find(letter)
        find = []
        while(i!=-1):
            find.append(i)
            i = word.find(letter,i+1)
        i = word.find(letter.upper())
        while(i!=-1):
            find.append(i)
            i = word.find(letter,i+1)
        combt = []
        for i in range(1, len(find)+1):
            comb=combinations(find, i)
            for j in list(comb):
                combt.append(j)
        for i in combt:
            tempwordlist.append(replace(word, list(i), letter))
            tempwordlist.append(replace(word, list(i), letter.upper()))
            tempwordlist.append(replace(word, list(i), sust))
        for i in tempwordlist:
            if i not in wordlist:
                changes+=1
                wordlist.append(i)

        wordlistindex+=1
    return wordlist