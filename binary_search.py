numbers = [1,2,3,4,5,6,7,8,9,10,11]#1000_0000
target = 110
iterations = 0
low = 0
high = len(numbers)-1
while low <= high:
    mid = (low + high) // 2
    if numbers[mid] == target:
        iterations += 1
        print(f'Target {target} found at index {mid}')
        break
    elif numbers[mid] < target:
        low = mid + 1
        iterations += 1
    else:
        high = mid - 1
        iterations += 1
else:
    print('Target not found')

print(f'You searched {iterations} times')