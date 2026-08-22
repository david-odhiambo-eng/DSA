#PROBLEM:
#Youa are given a list of numbers
#You are supposed to only square
#even numbers
#Then find the sum of those even numbers
#Use a for loop and list comprehension methods

#1. for loop
numbers = [10, 3, 2, 17, 30.4, 98, 8]
# squared_nums = []
sum = 0
# for num in numbers:
#     if num % 2 == 0:
#         squared_nums.append(num * num)
# print(squared_nums)
# for num in squared_nums:
#     sum += num
# print(sum)

#answer is: 9772

# 2. using list comprehension
squared_nums = [num * num for num in numbers if num % 2 == 0]
for num in squared_nums:
    sum += num
print(squared_nums)
print(sum)
