#while true sets a while loop that runs continously until a certain condition is met that would then lead to a break
while True:
    response = input('How many wives do you have?: ')
    if response == 'I have only one wife':
        break
    else:
        print('You got the answer wrong')
print('You got the answer right')