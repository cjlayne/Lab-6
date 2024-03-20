def main():
    while True:
        print('Menu')
        print('-------------')
        print('1. Encode')
        print('2. Decode')
        print('3. Quit')
        print()
        option = int(input('Please enter an option: '))

        if option == 1:
            password = int(input('Please enter your password to encode: '))
            password = encode(password)
            print('Your password has been encoded and stored!')
        elif option == 2:
            print(f'The encoded password is {password}, and the original password is {decode(password)}')
        elif option == 3:
            False
        else:
            print('Invalid option')
        

def encode(string):
    pass

def decode(string):
    pass

if __name__ == '__main__':
    main()