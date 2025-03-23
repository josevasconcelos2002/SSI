import sys
import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.ciphers.algorithms import ChaCha20


# setup <fkey>
def setup(fkey):
    key = os.urandom(32)  # ChaCha20 exige 32 bytes
    with open(fkey, 'wb') as file:
        file.write(key)
    print(f"Chave gerada e salva em: {fkey}")


# enc <fich> <fkey>
def enc(fich, fkey):
    try:
        
        with open(fich, "rb") as file1:
            content = file1.read()

        
        with open(fkey, "rb") as file2:
            key = file2.read().strip()

        
        if len(key) != 32:
            raise ValueError(f"Tamanho da chave inválido: {len(key)} bytes. A chave deve ter 32 bytes.")

        
        nonce = os.urandom(16)

        
        cipher = Cipher(ChaCha20(key, nonce), mode=None)
        encryptor = cipher.encryptor()
        
        
        encrypted = encryptor.update(content) + encryptor.finalize()

        
        output_file = fich + ".enc"

        # Salvar o NONCE no ficheiro de output
        with open(output_file, "wb") as file3:
            file3.write(nonce)
            file3.write(encrypted)

        print(f"Arquivo cifrado criado: {output_file}")

    except Exception as e:
        print(f"Erro ao cifrar o arquivo: {e}")


# dec <fich> <fkey>
def dec(fich, fkey):
    try:
        
        with open(fkey, "rb") as file2:
            key = file2.read().strip()

        
        if len(key) != 32:
            raise ValueError(f"Tamanho da chave inválido: {len(key)} bytes. A chave deve ter 32 bytes.")

        
        with open(fich, "rb") as file1:
            nonce = file1.read(16)  
            encrypted_content = file1.read() 

        
        cipher = Cipher(ChaCha20(key, nonce), mode=None)
        decryptor = cipher.decryptor()
        
        
        decrypted = decryptor.update(encrypted_content) + decryptor.finalize()

        
        output_file = fich.replace(".enc", ".dec")

        
        with open(output_file, "wb") as file3:
            file3.write(decrypted)

        print(f"Arquivo decifrado criado: {output_file}")

    except Exception as e:
        print(f"Erro ao decifrar o arquivo: {e}")



def main(argc, argv):
    if argc < 3:
        print("USAGE: python3 cfich_chacha20.py <operation> <args>")
        return
    
    operation = argv[1].lower()

    if operation == "setup":
        if argc == 3:
            setup(argv[2])
        else:
            print("USAGE: python3 cfich_chacha20.py setup <fkey>")
    
    elif operation == "enc":
        if argc == 4:
            enc(argv[2], argv[3])
        else:
            print("USAGE: python3 cfich_chacha20.py enc <fich> <fkey>")
    
    elif operation == "dec":
        if argc == 4:
            dec(argv[2], argv[3])
        else:
            print("USAGE: python3 cfich_chacha20.py dec <fich> <fkey>")
    
    else:
        print("Operação inválida. Utilize 'setup', 'enc' ou 'dec'.")


if __name__ == '__main__':
    main(len(sys.argv), sys.argv)
