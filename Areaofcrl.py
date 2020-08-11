# Program to find the area of circle if the entred value is > 0

r = int(input('Enter radius'))
if r > 0:
    area = 3.14*r*r
    print(area)
else:
    print('Enter valid value')
