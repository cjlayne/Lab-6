#Conner Layne
def main():
    while True:
        print('Menu')
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
    return ''.join(str((int(digit)+3)% 10) for digit in password)

#Justin Wild
def decode(string):
    return ''.join(str((int(digit) - 3) % 10) for digit in string)

if __name__ == '__main__':
    main()
