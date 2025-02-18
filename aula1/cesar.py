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