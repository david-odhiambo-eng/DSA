#Take user input, allow the user to only guess 5 times at most

guesses = 5
count = 0
answer = 'I only have one wife'

while True:
    response = input('How many wives do you have?: ')
    count += 1
    if response == answer:
        print(f'Correct, you have guessed {count} times')
        break
    elif guesses == 0:
        print('You are out of guesses...Bye')
        break
    else:
        guesses -= 1
        print(f'You have guessed {count} times, {guesses} guesses remaining')

print(f'You have guessed {count} times')

