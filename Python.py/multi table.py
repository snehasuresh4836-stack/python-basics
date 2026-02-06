# Input from user
num = int(input("Enter a number: "))

print(f"Multiplication table of {num}:")

# Loop from 1 to 10
for i in range(1, 21):
    print(f"{num} x {i} = {num * i}")
