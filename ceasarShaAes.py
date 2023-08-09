
import string
import hashlib
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

def userInputs():
    sourceCheck = False

    while True:
        eType = input(f'Enter the number of the encryption type you would like to apply:\n\t1. AES\n\t2. Ceasar\n\t3. SHA\nChoice (1-3): ')

        if eType in ('1','2','3'):
            eType = int(eType)
            sourceFile = input('Enter file for encryption: ')
            while sourceCheck == False:
                try:
                   filePointer = open(f'{sourceFile}','r')
                   sourceCheck = True
                   plainText = filePointer.read()
                   filePointer.close()
                   return eType, plainText, sourceFile 
                except:
                    print (f'Target file {sourceFile} cannot be openned, please try again.\n')
                    sourceFile = input('Enter file for encryption: ')
        else:
            print (f'\n\tInvalid option, please try again.\n')

def aesE (plainText, sourceFile):
    plainText = (plainText).encode('utf-8')
    key = get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(plainText)
    encryptedFile = open(f'encrypted_{sourceFile}.bin','wb')
    [encryptedFile.write(x) for x in (cipher.nonce, tag, ciphertext)]
    encryptedFile.close()
    print (f'File encrypted using the following key:\n\t{key}\n')

def ceasarE (plainText,sourceFile):
    letters = string.printable
    shift = 9

    cipherText = ""
    for letter in plainText:
        if letter in letters:
            index = letters.find(letter)
            cipherText += letters[(index + shift) % len(letters)]
        else:
            cipherText += letter    
   
    encryptedFile = open(f'encrypted_{sourceFile}.bin', 'w')
    encryptedFile.write(f'{cipherText}')
    encryptedFile.close()

def shaE (plainText, sourceFile):
    cipherText = hashlib.sha256(plainText.encode('utf-8')).hexdigest()
    
    encryptedFile = open(f'encrypted_{sourceFile}.bin', 'w')
    encryptedFile.write(f'{cipherText}')
    encryptedFile.close()



choice,plainText,sourceFile = userInputs()

if choice == 1:
   aesE(plainText,sourceFile)
elif choice == 2:
   ceasarE(plainText,sourceFile)
elif choice == 3:
    shaE(plainText,sourceFile)
