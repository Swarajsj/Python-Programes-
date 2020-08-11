# Program to revesers the number without using any loop

num = int(input())
r = num % 10
q = num // 10
r = (r*10)+(q % 10)
q = q // 10
r = (r*10)+(q % 10)
q = q // 10
r = (r*10)+(q % 10)
print(r)
