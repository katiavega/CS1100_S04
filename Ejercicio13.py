# Input
n = int(input("n: "))

inverso = 0
while n > 0:
    inverso = (inverso * 10) + (n % 10)
    n //= 10

print(inverso)
