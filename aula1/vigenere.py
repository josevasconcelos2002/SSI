import sys
from cesar_utils import preproc, encrypt, decipher


def vigenere_encrypt(secret_keys, message):
    encrypted_message = ""
    i = 0
    size = len(secret_keys)
    for char in message:
        encrypted_message += encrypt(secret_keys[i], char)
        i = (i+1) % size
    return encrypted_message

def vigenere_decipher(secret_keys, message):
    msg = ""
    i = 0
    size = len(secret_keys)
    for char in message:
        msg += decipher(secret_keys[i], char)
        i = (i+1) % size
    return msg




def main(argc, argv):
    if(argc < 4):
        print("USAGE: python3 vigenere.py <operation> <secret_keys> <message>")
    elif(argc == 4):
        
        operation = argv[1].lower()
        secret_keys = argv[2]
        message = preproc(argv[3])
        
        if operation == "enc":
            encrypted_message = vigenere_encrypt(secret_keys, message)
            print(encrypted_message)
            
        elif operation == "dec":
            msg = vigenere_decipher(secret_keys, message)
            print(msg)
        
    

if __name__ == '__main__':
    main(len(sys.argv), sys.argv)