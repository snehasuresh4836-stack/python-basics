import math

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# HCF (GCD)
hcf = math.gcd(a, b)

# LCM formula
lcm = (a * b) // hcf

print("HCF:", hcf)
print("LCM:", lcm)
