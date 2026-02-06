


arr_input = input("Enter numbers separated by spaces: ")

# Convert the input string into a list of numbers
arr = list(map(int, arr_input.split()))

# Initialize sum
total = 0

# Loop through the array to calculate sum
for num in arr:
    total += num


print("Sum of the array elements:", total)
