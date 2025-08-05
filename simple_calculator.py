# simple_calculator for python

def add(x, y):
    """Return the sum of x and y"""
    return x + y


def subtract(x, y):
    """Return the difference of x and y."""
    return x - y


def multiply(x, y):
    """Return the product of x and y."""
    return x * y


def divide(x, y):
    """Return the division of x by y. Raises ZeroDivisionError if y is zero."""
    if y == 0:
        raise ZeroDivisionError("Cannot divide by zero!")
    return x / y


def main():
    print("Welcome to the Simple Calculator!")
    print("Operations: +, -, *, /")

    while True:
        try:
            num1 = float(input("Enter the first number: "))
            operator = input("Enter the operator (+, -, *, /): ")
            num2 = float(input("Enter the second number: "))

            if operator == '+':
                result = add(num1, num2)
            elif operator == '-':
                result = subtract(num1, num2)
            elif operator == '*':
                result = multiply(num1, num2)
            elif operator == '/':
                result = divide(num1, num2)
            else:
                print("Invalid operator! Please try again.")
                continue

            print(f"Result: {num1} {operator} {num2} = {result}\n")

        except ValueError:
            print("Invalid input! Please enter numeric values.\n")
            continue
        except ZeroDivisionError as e:
            print(f"Error: {e}\n")
            continue

        cont = input("Do you want to calculate again? (y/n): ").lower()
        if cont != 'y':
            print("Thanks for using the calculator. Goodbye!")
            break


if __name__ == "__main__":
    main()

