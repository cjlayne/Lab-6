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
            password = input('Please enter your password to encode: ')
            password = encode(password)
            print('Your password has been encoded and stored!')
        elif option == 2:
            print(f'The encoded password is {password}, and the original password is {decode(password)}')
        elif option == 3:
            False
        else:
            print('Invalid option')
        

def encode(password):
    encoded_password = []
    for num in password:
        num = int(num)
        num += 3
        if num >= 10:
            num-= 10
        encoded_password.append(str(num))
    encoded_password = ''.join(encoded_password)
    return encoded_password


def decode(string):
    pass

if __name__ == '__main__':
    main()