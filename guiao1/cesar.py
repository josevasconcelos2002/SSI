import sys
from cesar_utils import preproc, encrypt, decipher



def main(argc, argv):
    if(argc < 4):
        print("USAGE: python3 cesar.py <operation> <secret_key> <message>")
    elif(argc == 4):
        
        operation = argv[1].lower()
        secret_key = argv[2]
        message = preproc(argv[3])
        
        if operation == "enc":
            msg = encrypt(secret_key, message)
            print(msg)
        elif operation == "dec":
            msg1 = decipher(secret_key, message)
            print(msg1)
        
    

if __name__ == '__main__':
    main(len(sys.argv), sys.argv)