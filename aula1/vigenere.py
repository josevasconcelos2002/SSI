import sys
from cesar_utils import preproc, encrypt, decipher

def main(argc, argv):
    if(argc < 4):
        print("USAGE: python3 vigenere.py <operation> <secret_keys> <message>")
    elif(argc == 4):
        
        operation = argv[1].lower()
        secret_keys = argv[2]
        message = preproc(argv[3])
        
        if operation == "enc":
            encrypted_message = ""
            i = 0
            size = len(secret_keys)
            for char in message:
                encrypted_message += encrypt(secret_keys[i], char)
                i = (i+1) % size
            print(encrypted_message)
            
        elif operation == "dec":
            msg = ""
            i = 0
            size = len(secret_keys)
            for char in message:
                msg += decipher(secret_keys[i], char)
                i = (i+1) % size
            print(msg)
        
    

if __name__ == '__main__':
    main(len(sys.argv), sys.argv)