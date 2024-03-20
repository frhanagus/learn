text = 'a quick brown fox jumps over the lazy dog'.upper()

def count_letters(string):
    counter = [0]*26
    ctr = 0
    for letter in string :
        if letter.isalpha() == True :
            counter[ord(letter)-65] += 1
    print (counter)

    for i in range(26) :
        if counter[i] != 0:
            ctr += 1
        print(f'{chr(i+65)} : {counter[i]}')
    print()
    if ctr == 26:
        print ('sentence is a panggram')

count_letters(text)