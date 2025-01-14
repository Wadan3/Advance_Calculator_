import math
def show_menu():
    print("Welcome to the Advanced Calculator!")
    print("Select an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Power (^)")
    print("6. Square Root (√)")
    print("7. Logarithm (log)")
    print("8. Sine (sin)")
    print("9. Cosine (cos)")
    print("10. Tangent (tan)")
    print("11. Exit")

def perform_operation(choice):
    try:
        if choice in {'1', '2', '3', '4', '5'}:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            
            if choice == '1':
                print(f"Result: {num1 + num2}")
            elif choice == '2':
                print(f"Result: {num1 - num2}")
            elif choice == '3':
                print(f"Result: {num1 * num2}")
            elif choice == '4':
                if num2 == 0:
                    print("Error: Division by zero is not allowed.")
                else:
                    print(f"Result: {num1 / num2}")
            elif choice == '5':
                print(f"Result: {num1 ** num2}")

        elif choice == '6':
            num = float(input("Enter the number: "))
            if num < 0:
                print("Error: Cannot calculate square root of a negative number.")
            else:
                print(f"Result: {math.sqrt(num)}")

        elif choice == '7':
            num = float(input("Enter the number: "))
            if num <= 0:
                print("Error: Logarithm only defined for positive numbers.")
            else:
                base = input("Enter the base (default is e): ")
                if base == "":
                    print(f"Result: {math.log(num)}")
                else:
                    base = float(base)
                    print(f"Result: {math.log(num, base)}")

        elif choice in {'8', '9', '10'}:
            angle = float(input("Enter the angle in degrees: "))
            radians = math.radians(angle)
            
            if choice == '8':
                print(f"Result: {math.sin(radians)}")
            elif choice == '9':
                print(f"Result: {math.cos(radians)}")
            elif choice == '10':
                print(f"Result: {math.tan(radians)}")

        else:
            print("Invalid choice. Please select a valid option.")

    except ValueError:
        print("Error: Invalid input. Please enter numeric values where required.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-11): ")
        if choice == '11':
            print("Exiting the calculator. Goodbye!")
            break
        perform_operation(choice)
        print("\n")

if __name__ == "__main__":
    main()
