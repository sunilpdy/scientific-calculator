import math
from calculator import calculate


def get_number(prompt):
    value = float(input(prompt))

    if not math.isfinite(value):
        raise ValueError("Please enter a finite number")

    return value


def main():
    print("=" * 35)
    print("      SCIENTIFIC CALCULATOR")
    print("=" * 35)

    print("""
BASIC OPERATIONS
  +   Addition
  -   Subtraction
  *   Multiplication
  /   Division
  ^   Power
  %   Percentage (a% of b)

SCIENTIFIC OPERATIONS
  sqrt  Square root
  sin   Sine (degrees)
  cos   Cosine (degrees)
  tan   Tangent (degrees)
  ln    Natural logarithm
  log   Logarithm base 10
  exp   e raised to a power
  fact  Factorial
  inv   Reciprocal
  abs   Absolute value

Type q to exit.
""")

    while True:
        try:
            operator = input("Choose operation: ").strip().lower()

            if operator == "q":
                print("Thank you for using the calculator!")
                break

            if operator in {
                "sqrt", "sin", "cos", "tan", "ln",
                "log", "exp", "fact", "inv", "abs"
            }:
                a = get_number("Enter number: ")
                result = calculate(operator, a)

            elif operator in {"+", "-", "*", "/", "^", "%"}:
                a = get_number("Enter first number: ")
                b = get_number("Enter second number: ")
                result = calculate(operator, a, b)

            else:
                print("Invalid operation. Please try again.")
                continue

            if not math.isfinite(result):
                print("Error: Result is outside the supported range.")
                continue

            print(f"Result: {result:.10g}")

        except ValueError as error:
            print(f"Error: {error}")

        except OverflowError:
            print("Error: Result is too large.")

        except (KeyboardInterrupt, EOFError):
            print("\nCalculator closed.")
            break


if __name__ == "__main__":
    main()
