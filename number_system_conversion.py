

n = int(input("Enter a decimal number: "))

# Decimal to Binary
temp = n
binary = ""
while temp > 0:
    binary = str(temp % 2) + binary
    temp = temp // 2

# Decimal to Octal 
temp = n
octal = ""
while temp > 0:
    octal = str(temp % 8) + octal
    temp = temp // 8

#  Decimal to Hexadecimal 
temp = n
hex_digits = "0123456789ABCDEF"
hexa = ""
while temp > 0:
    hexa = hex_digits[temp % 16] + hexa
    temp = temp // 16


print("\nDecimal Number   :", n)
print("Binary Equivalent:", binary)
print("Octal Equivalent :", octal)
print("Hex Equivalent   :", hexa)
