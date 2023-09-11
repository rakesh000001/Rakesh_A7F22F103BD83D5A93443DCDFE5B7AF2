# Recursive function to calculate factorial
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Input from the user
num = int(input("Enter a non-negative integer: "))

# Check if the input is valid
if num < 0:
    print("Please enter a non-negative integer.")
else:
    result = factorial(num)
    print(f"{num}! = {result}")