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