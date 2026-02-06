
arr = list(map(int, input("Enter numbers separated by space: ").split()))


largest = arr[0]

# Compare with remaining elements
for num in arr:
    if num > largest:
        largest = num


print("Largest number in the array is:", largest)
