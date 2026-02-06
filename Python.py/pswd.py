password = input("Enter your password: ")

has_upper = False
has_lower = False
has_digit = False
has_special = False

special_chars = "@#$%&*"

# Check length first
if len(password) < 8:
    print("Password must be at least 8 characters long.")
else:
    # Check each character
    for ch in password:
        if ch.isupper():
            has_upper = True
        elif ch.islower():
            has_lower = True
        elif ch.isdigit():
            has_digit = True
        elif ch in special_chars:
            has_special = True

    # Final check
    if has_upper and has_lower and has_digit and has_special:
        print("Password is VALID")
    else:
        print("Password is INVALID")
        if not has_upper:
            print("- Add at least one uppercase letter")
        if not has_lower:
            print("- Add at least one lowercase letter")
        if not has_digit:
            print("- Add at least one digit")
        if not has_special:
            print("- Add at least one special character (@#$%&*)")
