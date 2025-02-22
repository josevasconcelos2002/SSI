import sys
from cesar_utils import preproc


def main(argc, argv):
    if(argc < 4):
        print("USAGE: python3 vigenere.py <operation> <secret_keys> <message>")
    elif(argc >= 4):
        
        secret_keys_length = argv[1]
        cryptograma = argv[2]
        words = []
        # number of words
        lefting = argc - 3
        for i in lefting:
            words.append(argv[i])
        
        
        
    

if __name__ == '__main__':
    main(len(sys.argv), sys.argv)