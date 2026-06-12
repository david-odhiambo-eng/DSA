# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

 

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]

nums: list = [2,10,23,410.5,13,4,15,55,100]
target: int = 510.5
demo: dict = {}

#we first use brute force, which involves iterating through the entire list
#we use two loops
#the first loop iterates from index 0 to the last
#second loop iterates from index 1 to last 
#the two loops are nested, meaning they run at the same time

for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        if nums[i] + nums[j] == target:
            demo['first_number'] = nums[i]
            demo['second_number'] = nums[j]
            demo['indices'] = [i, j]
print(f'First number: {demo['first_number']}\nSecond number: {demo['second_number']}\nIndices: {demo['indices']}')