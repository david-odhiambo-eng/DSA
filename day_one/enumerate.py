#enumerate gives you both the index and value of an iterable
#iterables includes lists etc

name: list = ['David', 'Natasha', 'Jesse', 'Flutter']

for index, value in enumerate(name):
    print(index, value)

print('......................\n')

cars: list = ['Auidi', 'BMW', 'Nissan', 'Tesla']

for index, car in enumerate(cars, start=1):
    print(index, car)

print('......................\n')

for index, value in enumerate(name):
    print(f'{index+2}', value)