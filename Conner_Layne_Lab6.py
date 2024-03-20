#Conner Layne
def main():
    while True:
        print('\nMenu')
        print('-------------')
        print('1. Encode')
        print('2. Decode')
        print('3. Quit')
        print()
        try:
            option = int(input('Please enter an option: '))
        except:
            print('Please input a valid option')

        if option == 1:
            password = input('Please enter your password to encode: ')
            password = encode(password)
            print('Your password has been encoded and stored!')
        elif option == 2:
            print(f'The encoded password is {password}, and the original password is {decode(password)}.')
        elif option == 3:
            break
        else:
            print('Please input a valid option')
        

def encode(password):
    return ''.join(str((int(digit) + 3)% 10) for digit in password)


# Yazan Al-Hawamdeh
def decode(encoded_password):
    decoded_password = ""
    for digit in encoded_password:
        decoded_digit = (int(digit) - 3) % 10
        decoded_password += str(decoded_digit)
    return decoded_password


if __name__ == '__main__':
    main()
