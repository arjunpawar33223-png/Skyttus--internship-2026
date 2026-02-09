balance = 10000
amount = int(input("Enter withdrawal amount: "))

if amount <= balance:
    print("Withdrawal successful")
else:
    print("Insufficient balance")