first = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
second = float(input("Enter second number: "))

if operator == "+":
    print("Result:", first + second)
elif operator == "-":
    print("Result:", first - second)
elif operator == "*":
    print("Result:", first * second)
elif operator == "/":
    if second != 0:
        print("Result:", first / second)
    else:
        print("Cannot divide by zero.")
else:
    print("Invalid operator.")
