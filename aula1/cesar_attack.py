import sys


def preproc(str):
 l = []
 for c in str:
    if c.isalpha():
        l.append(c.upper())
 return "".join(l) 



def encrypt(secret_key, message):
    msg = ""
    start = ord('A')
    key = ord(secret_key) - start  # Convert key character to ASCII
    #print("Secret_key ord: " + str(key))
    
    for c in message:
        dif = (start + (ord(c) - start + key) %26)
        msg += chr(dif)

    return msg  # Return the encrypted message
        
    
def decipher(secret_key, message):
    msg = ""
    start = ord('A')
    key = ord(secret_key) - start  # Convert key character to ASCII
    #print("Secret_key ord: " + str(key))
    
    for c in message:
        dif = dif = start + (ord(c) - start - key) % 26
        msg += chr(dif)
        #print(msg)

    return msg  # Return the encrypted message


def attack(encrypted_message, word1, word2):
    letters = [chr(i) for i in range(ord('B'), ord('Z')+1)]
    
    for letter in letters:
        msg = decipher(letter, encrypted_message)
        if(word1 in msg or word2 in msg):
            print(letter + "\n" + msg)


def main(argc, argv):
    if(argc < 4):
        print("USAGE: python3 cesar.py <operation> <secret_key> <message>")
    elif(argc == 4):
        
        encrypted_message = argv[1]
        word1 = argv[2]
        word2 = preproc(argv[3])
        
        attack(encrypted_message, word1, word2)
        
    

if __name__ == '__main__':
    main(len(sys.argv), sys.argv)