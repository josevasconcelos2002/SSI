def main(argc, argv):
    if(argc < 3):
        print("USAGE: python3 cfich_chacha20.py <operation> <args>")
    elif(argc > 3):
        
        operation = argv[1].lower()
        
        if(operation == "setup"):
            fkey = argv[2]
            
        elif(operation == "enc"):
            fich = argv[2]
            fkey = argv[3]
        
        elif(operation == "dec"):
            fich = argv[2]
            fkey = argv[3]
        
if __name__ == '__main__':
    main(len(sys.argv), sys.argv)