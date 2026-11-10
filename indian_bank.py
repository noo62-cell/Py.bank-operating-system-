print("Indian Bank Software System")

login = input("Email ID: ")
print("Welcome to Indian Bank - Nagpur Branch")
print("\nATM Machine")
print("\nIndian Bank")

# PIN login
password = ""
while password != "1234":
    password = input("Enter PIN: ")
    if password != "1234":
        print("Wrong PIN. Try again.")

print("Unlocked!")
print("Withdrawal")
print("Deposit")

# Banking system
while True:
    choice = input("\nWhich A/C? (Press 'd' to exit): ").lower()

    if choice == "d":
        break

    try:
        balance = float(input("Enter your current balance: "))
        deposit = float(input("Deposit cash: "))
        withdrawal = float(input("Withdrawal cash: "))

        balance = balance + deposit - withdrawal
        total = balance

        print(f"\nYour balance: {balance}")
        print(f"Deposit cash: {deposit}")
        print(f"Withdrawal cash: {withdrawal}")
        print(f"Total balance: {total}")

        print("\nPrinted Receipt")
        print("Indian Bank Receipt")
        print("Withdrawal:", withdrawal)
        print("Total:", total)

    except ValueError:
        print("Please enter valid numbers.")

# Account opening system
print("\nAccount Open System")
name = input("Name: ")
surname = input("Surname: ")
aadhar = input("Aadhar No: ")
mob = input("Mobile No: ")
address = input("Address: ")
pan = input("PAN No: ")

print("Welcome to Indian Bank", name)
print("Your account number is 775776787")

# KYC system
print("\nKYC System")

while True:
    kyc_name = input("Name (type 'off' to exit): ")

    if kyc_name.lower() == "off":
        break

    ac = input("A/C Number: ")
    aadhar = input("Aadhar Number: ")
    phone = input("Phone No: ")

    print("KYC Successfully Completed")

# Calculator
print("\nIndian Bank Calculator")

try:
    a = float(input("Enter number: "))
    op = input("Operator (+, -, *, /): ")
    b = float(input("Next number: "))

    if op == "+":
        print(a + b)
    elif op == "-":
        print(a - b)
    elif op == "*":
        print(a * b)
    elif op == "/":
        if b == 0:
            print("Cannot divide by zero.")
        else:
            print(a / b)
    else:
        print("Wrong operator")

except ValueError:
    print("Please enter valid numbers.")

print("\nThank you for using Indian Bank Software System!")
