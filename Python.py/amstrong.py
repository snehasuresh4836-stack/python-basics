# Input from user
num = int(input("Enter a number: "))

# Convert number to string to get digits
digits = str(num)

sum = 0

# Loop through each digit
for digit in digits:
    sum += int(digit) ** len(digits)  # Raise to power of number of digits

# Check if sum equals the original number
if sum == num:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")
