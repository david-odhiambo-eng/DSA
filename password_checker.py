#taking user password, display ****
import msvcrt

# password strength checker
# Length = 8      ✅
# Uppercase    ✅
# Numbers      ✅
# Symbols      ✅
def check_password_strength(password: str)->str:
    #checking length
    is_long = len(password)>=8
    #checking uppercase
    has_upper=any(char.isupper() for char in password)
    #number check
    has_num=any(char.isalnum() for char in password)
    #checking for symbols
    symbols = ['.','!', '?', '/', ',']
    has_symbol=any(char for char in password if char in symbols)
    score = sum([is_long,has_num,has_upper,has_symbol])
    #True=1, False=0
    if score == 4:
        print("Password Strength: 🟩🟩🟩🟩...100%")
    elif score == 3:
        print("Password Strength: 🟩🟩🟩...75%")
    elif score == 2:
        print("Password Strength: 🟩🟩...50%")
    else:
        print("Password Strength: 🟩...25%")


def capture_password():
    print('Enter password: ',end='',flush=True)
    password = ''
    while True:
        #taking user input and outputing it immediately
        character: bytes = msvcrt.getch()
        #checking for enter key
        if character == b'\r':
            break
        password += character.decode('utf-8')
        print('*',end='',flush=True)
    print(f'\nYour password is: {password}')
    check_password_strength(password=password)

capture_password()