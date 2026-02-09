try:
    email = input("Enter email: ")
    if "@" not in email or "." not in email:
        raise ValueError("Invalid email format")
    print("Valid email")
except ValueError as e:
    print(e)