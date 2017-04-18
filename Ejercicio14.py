# Input
original = int(input("n: "))

n = original
inverso = 0
while n > 0:
    inverso = (inverso * 10) + (n % 10)
    n //= 10

print(original == inverso);
