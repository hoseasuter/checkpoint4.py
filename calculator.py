import math


def exponentiation(a, b):
    """Return a raised to the power of b."""
    return math.pow(a, b)


def square_root(a, _=None):
    """Return the square root of a."""
    return math.sqrt(a)


def logarithm(a, _=None):
    """Return the natural logarithm of a."""
    return math.log(a)


def sine(a, _=None):
    """Return the sine of a (angle in radians)."""
    return math.sin(a)


def cosine(a, _=None):
    """Return the cosine of a (angle in radians)."""
    return math.cos(a)


def tangent(a, _=None):
    """Return the tangent of a (angle in radians)."""
    return math.tan(a)


class Calculator:
    def __init__(self):
        """Initialize the calculator with basic operations."""
        self.operations = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: a / b,
        }

    def add_operation(self, symbol, func):
        """Add a new operation and its corresponding function."""
        self.operations[symbol] = func

    def calculate(self, num1, operation, num2):
        """Perform a calculation based on the operation symbol."""
        if not isinstance(num1, (int, float)):
            print("Error: The first input is not a valid number.")
            raise TypeError("Invalid input: num1 must be a number.")

        if not isinstance(num2, (int, float)):
            print("Error: The second input is not a valid number.")
            raise TypeError("Invalid input: num2 must be a number.")

        if operation not in self.operations:
            print(f"Error: '{operation}' is not a valid operation.")
            raise ValueError(f"Invalid operation: '{operation}' is not supported.")

        func = self.operations[operation]
        return func(num1, num2)


def main():
    calc = Calculator()

    # Add advanced operations
    calc.add_operation("**", exponentiation)
    calc.add_operation("sqrt", square_root)
    calc.add_operation("log", logarithm)
    calc.add_operation("sin", sine)
    calc.add_operation("cos", cosine)
    calc.add_operation("tan", tangent)

    print("Welcome to the Calculator!")
    print("Available operations: +, -, *, /, ** (exponentiation), sqrt (square root), log (natural logarithm), sin, cos, tan")
    print("Type 'exit' at any prompt to quit.\n")

    while True:
        first_input = input("Enter the first number (or 'exit' to quit): ")
        if first_input.lower() == "exit":
            break

        operation = input("Enter the operation symbol: ")
        if operation.lower() == "exit":
            break

        second_input = input("Enter the second number (or 'exit' to quit): ")
        if second_input.lower() == "exit":
            break

        try:
            num1 = float(first_input)
            num2 = float(second_input)
            result = calc.calculate(num1, operation, num2)
            print(f"Result: {result}\n")
        except (ValueError, TypeError, ZeroDivisionError) as e:
            print(f"Calculation failed: {e}\n")
        except Exception as e:
            print(f"An unexpected error occurred: {e}\n")

    print("Goodbye!")


if __name__ == "__main__":
    main()
