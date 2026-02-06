def square_of_digits(num):
   
    #Convert number to string 
    num_str = str(num)
    
    #store squares
    squares = []
    
    # Loop through each character (digit)
    for digit in num_str:
        squares.append(int(digit) ** 2)  # Convert back to int and square it
    
    return squares

# Example usage
number = int(input("Enter a number: "))
result = square_of_digits(number)
print("Squares of digits:", result)

