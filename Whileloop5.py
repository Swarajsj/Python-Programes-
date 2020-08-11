# Program to print the sum of the numbers from 1 to 20 and that is divisible by 5

count = 1
sum = 0
while count <= 20:
    if count % 5 == 0:
        sum = sum + count
    count = count + 1
print(sum)
