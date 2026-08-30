#creating the sum() method from scratch
def calculate_sum(numbers: list):
    sum = 0
    for num in numbers:
        sum += num
    return sum


sum = calculate_sum([1,2,3,4,5,])
print(f'Sum is: {sum}')