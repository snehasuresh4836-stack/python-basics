# Input from user
n = int(input("Enter a number: "))

factorial = 1  # Start with 1, because 0! = 1

if n < 0:
    print("Factorial does not exist for negative numbers")
else:
    # Multiply all numbers from 1 to n
    for i in range(1, n + 1):
        factorial *= i
    print("Factorial of", n, "is", factorial)
