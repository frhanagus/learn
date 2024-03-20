#alphabet = []
#for i in range(26) :
 #   alphabet.append(chr(i+65))
#print (alphabet)

string = 'a quick brown fox jumps over the lazy dog'

def count_letters(string):
    counter = [0]*26
    for letter in string :
        counter[ord(letter)-65] += 1
    print (counter)

    for i in range(26) :
        print(f'{chr(i+65)} : {counter[i]}')
    print()

def is_palindrome(string) :
    string = string.upper()
    string = string.replace(',', '')
    string = string.replace(' ', '')
    n = len(string)//2
    for i in range (n) :
        if string[i] != string[n-i-1] :
            return False
    return True

strings = ['a quick brown fox jumps over the lazy dog',
            'a man, a plan, a canal, Panama',
            'Beasiswa Indonesia maju']
a = 'RACECAR'

# for str in strings:
# count_letters(str.upper())
for str in strings:
    print ( is_palindrome(a)
    )