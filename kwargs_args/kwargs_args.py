#adding multiple numbers
def add_many_numbers(*args):
    #args is of type tuple
    sum = 0
    for num in args:
        sum += num
    return sum

total_sum = 0
while True:
    number = input('Enter number: ')
    total_sum += add_many_numbers(int(number))
    print(f'Total sum is {total_sum}\n')
    if total_sum >= 150:
        break
print(f'Total sum is now {total_sum}')