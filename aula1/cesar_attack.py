import sys
from cesar_utils import preproc, decipher


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