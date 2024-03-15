# ATTACKATFIVE
def encrypt():
    for i in text :
        encrypting = ord(i) + 2 
        print (chr(encrypting).upper(), end='')
        
def decrypt():
    for i in code :
        decrypting = chr(i) - 2 
        print (ord(decrypting).upper(), end='')

print ("Caesar Cipher encryptor and decryptor")
choice = int(input("What can i do for you?\n1. Encrypt Text\n2. Decrypt Code\n: "))

if choice == 1 :
    text = input('Input text to encrypt: ').upper()
    print (f"encrypted text: ", encrypt())
elif choice == 2 :
    code = input('Input code to decrypt: ').upper()
    print (f'decypted text: ', decrypt())
else :
    print ("Please choose 1 or 2")