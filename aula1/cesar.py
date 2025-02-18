import sys


def encrypt(secret_key, message):
    l = []
    for c in message:
        if c.isalpha():
            l.append(c.upper())
    "".join(l)
    
def decipher(secret_key, message):
    print(secret_key, message)



def main(argc, argv):
    if(argc < 4):
        print("USAGE: python3 cesar.py <operation> <secret_key> <message>")
    elif(argc == 4):
        operation = argv[1].lower()
        secret_key = argv[2]
        message = argv[3]
        if operation == "enc":
            encrypt(secret_key, message)
        elif operation == "dec":
            decipher(secret_key, message)
        
    

if __name__ == '__main__':
    main(len(sys.argv), sys.argv)