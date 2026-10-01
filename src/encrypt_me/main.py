from encrypt_me.encryption import encrypt
from sys import argv

def main() :
    if len(argv) == 1 :
        text = input('enter text: ')

    elif len(argv) > 1 :
        text = argv[1]

    encrypted_text = encrypt(text)
    print(encrypted_text)

if __name__ == "__main__" :
    main()
