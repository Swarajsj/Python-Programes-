# Program to print the graeter number between four digits

num1 = int(input("Enter value for 1 :"))
num2 = int(input("Enter value for 2 :"))
num3 = int(input("Enter value for 3 :"))
num4 = int(input("Enter value for 4 :"))
sum = num1 + num2 + num3 + num4
for i in range(sum):
    if i == num1 or i == num2 or i == num3 or i == num4:
        l = i
print("Greater Number is :", l)
