n = int(input("Enter a number: "))

square = n * n
sum_digits = 0

while square > 0:
    digit = square % 10
    sum_digits += digit
    square //= 10

if sum_digits == n:
    print("Neon number")
else:
    print("Not a Neon number")