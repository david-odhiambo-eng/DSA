num = 842000
squares = []
sum = 0

for i in range(num):
    if i % 2 == 1:
        squares.append(i)
for j in squares:
    s = j * j
    sum += s

print(sum)
