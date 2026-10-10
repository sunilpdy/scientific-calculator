from scientific_operations import (
    add, subtract, multiply, divide, power,
    square_root, factorial, sine, cosine, tangent,
    natural_log, log_base_10, exponential,
    reciprocal, absolute, percentage
)


UNARY_OPERATIONS = {
    "sqrt": square_root,
    "sin": sine,
    "cos": cosine,
    "tan": tangent,
    "ln": natural_log,
    "log": log_base_10,
    "exp": exponential,
    "fact": factorial,
    "inv": reciprocal,
    "abs": absolute,
}

BINARY_OPERATIONS = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "^": power,
    "%": percentage,
}


def calculate(operator, a, b=None):
    if operator in UNARY_OPERATIONS:
        if b is not None:
            raise ValueError("This operation requires only one number")
        return UNARY_OPERATIONS[operator](a)

    if operator in BINARY_OPERATIONS:
        if b is None:
            raise ValueError("This operation requires two numbers")
        return BINARY_OPERATIONS[operator](a, b)

    raise ValueError("Unsupported operation")
