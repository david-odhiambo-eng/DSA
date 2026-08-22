#guessing game
correct_answer = 'Python'
guesses = 0
tries = 5

while True:
    try:
        attempt = input('Enter favorite language: ')
        if attempt == correct_answer:
            guesses += 1
            tries -= 1
            print('Correct...Hooray')
            break
        elif tries == 0:
            print('No guesses remaining')
            break
        else:
            guesses += 1
            tries -= 1
            print(f'{tries} remaining')
    except:
        print('Letters only')
print(f'You tried {guesses} times')