# F1: Sum of Digits

# Take input from the user
N = int(input("Enter an integer: "))

# Initialize sum
sum_of_digits = 0

# Use a loop to find the sum of digits
temp = abs(N)  # handle negative numbers
while temp > 0:
    digit = temp % 10
    sum_of_digits += digit
    temp //= 10

print("Sum of digits:", sum_of_digits)
