#creates an add function
def add(x, y):
    return x + y

#creates a subtraction function
def subtract(x, y):
    return x - y

#creates a multiplication function
def multiply(x, y):
    return x * y

#creates a division function
def divide(x, y):
    return x / y

print("Select an operation")
print("1. Add")
print("2. Subtract")
print("3. Multiplication")
print("4. Division")

while True:
    #select operation
    choice = input("Choose your operator (1/2/3/4): ")

    #checks if choice is one of the four options
    if choice in (' 1 ' ' 2 ' ' 3 ' ' 4 '):
        try:
            #float lets the user choose a fractured number
            n1 = float(input("Enter your first number: "))
            n2 = float(input("Enter your second number: "))
        except ValueError:
            print("Invalid Input. Please enter a number.")
            continue

        if choice == '1':
            print(n1, "+", n2, "=", add(n1, n2))
        
        elif choice == '2':
            print(n1, "-", n2, "=", subtract(n1, n2))

        elif choice == '3':
            print(n1, "*", n2, "=", multiply(n1, n2))

        elif choice == '4':
            print(n1, "/", n2, "=", divide(n1, n2))

         # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
          break
    else:
        print("Invalid Input")

