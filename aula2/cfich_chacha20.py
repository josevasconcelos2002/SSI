import sys
import os
import re
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding


# setup <fkey>
def setup(fkey):
    key = os.urandom(32)
    with open(fkey, 'wb') as file:
        file.write(key)
    print(f"Chave gerada e salva em: {fkey}")


# enc <fich> <fkey>
def enc(fich, fkey):
    try:
        # Ler o conteúdo do arquivo a ser cifrado
        with open(fich, "r") as file1:
            content = "".join(file1).encode()

        # Ler a chave do arquivo em modo binário
        with open(fkey, "rb") as file2:
            key = file2.read().strip()

        # Verificar o tamanho da chave
        key_length = len(key)
        if key_length not in (16, 24, 32):
            raise ValueError(f"Tamanho da chave inválido: {key_length} bytes. A chave deve ter 16, 24 ou 32 bytes.")

        iv = os.urandom(16)

        cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
        encryptor = cipher.encryptor()

        padder = padding.PKCS7(algorithms.AES.block_size).padder()
        padded_data = padder.update(content) + padder.finalize()

        encrypted = encryptor.update(padded_data) + encryptor.finalize()

        output_file = fich+".enc"
        print(f"Arquivo de saída: {output_file}")
        with open(output_file, "wb") as file3:
            file3.write(iv) 
            file3.write(encrypted)
        print(f"Arquivo cifrado criado: {output_file}")
    except Exception as e:
        print(f"Erro ao cifrar o arquivo: {e}")



# dec <fich> <fkey>
def dec(fich, fkey):
    try:
        # Ler a chave do arquivo em modo binário
        with open(fkey, "rb") as file2:
            key = file2.read().strip()

        # Verificar o tamanho da chave
        key_length = len(key)
        if key_length not in (16, 24, 32):
            raise ValueError(f"Tamanho da chave inválido: {key_length} bytes. A chave deve ter 16, 24 ou 32 bytes.")

        # Ler o conteúdo do arquivo cifrado
        with open(fich, "rb") as file1:
            iv = file1.read(16)  # O IV foi armazenado no início do arquivo
            encrypted_content = file1.read()

        # Configurar a cifra AES no modo CBC
        cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
        decryptor = cipher.decryptor()

        # Decifrar os dados
        decrypted_padded = decryptor.update(encrypted_content) + decryptor.finalize()

        # Remover o padding PKCS7
        unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
        decrypted = unpadder.update(decrypted_padded) + unpadder.finalize()

        # Criar o arquivo de saída
        if fich.endswith(".enc"):
            output_file = fich[:-4] + ".dec"
        else:
            output_file = fich + ".dec"

        with open(output_file, "wb") as file3:
            file3.write(decrypted)

        print(f"Arquivo decifrado criado: {output_file}")

    except Exception as e:
        print(f"Erro ao decifrar o arquivo: {e}")



def main(argc, argv):
    if(argc < 3):
        print("USAGE: python3 cfich_chacha20.py <operation> <args>")
    elif(argc >= 3):
        
        operation = argv[1].lower()
        
        if(operation == "setup"):
            if(argc == 3):
                fkey = argv[2]
                setup(fkey)
            else:
                print("USAGE: python3 cfich_chacha20.py setup <fkey>")
            
        elif(operation == "enc"):
            if(argc == 4):
                fich = argv[2]
                fkey = argv[3]
                enc(fich, fkey)
            else:
                print("USAGE: python3 cfich_chacha20.py enc <fich> <fkey>")
        
        elif(operation == "dec"):
            if(argc == 4):
                fich = argv[2]
                fkey = argv[3]
                dec(fich, fkey)
            else:
                print("USAGE: python3 cfich_chacha20.py dec <fich> <fkey>")

        
if __name__ == '__main__':
    main(len(sys.argv), sys.argv)