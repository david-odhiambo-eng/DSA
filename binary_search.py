values = [10,44,9.5,3,100,19,58]
sorted_values = sorted(values)
print(sorted_values)

low = 0
high = len(sorted_values)-1
target = 100
iteration = 0

while True:
    
    
    mid = (low + high) // 2
    print(f'Iteration {iteration}, Low: {low}, High: {high}, mid is at index {mid}')
    iteration += 1
    if sorted_values[mid] == target:
        print(f'Target {target} found at index {mid}')
        break
    elif sorted_values[mid] < target:
        print(f'Value: {sorted_values[mid]} is smaller than {target}')
        low = mid + 1
    elif low > high:
        break
    else:
        high = mid - 1
        print(f'Value {sorted_values[mid]} is larger than target')