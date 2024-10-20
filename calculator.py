num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

print("Choose the operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiply")
print("4. Devide")

choice = int(input("Enter the number of the operation you want to perform: "))

if choice == 1:
    result = num1 + num2
    print("Result:", result)
elif choice == 2:
    result = num1 - num2
    print("Result:", result)
elif choice == 3:
    result = num1 * num2
    print("Result:", result)
elif choice == 4:
    if num2 != 0:  # Avoid division by zero
        result = num1 / num2
        print("Result:", result)
    else:
        print("Cannot divide by zero!")
else:
    print("Invalid choice")
