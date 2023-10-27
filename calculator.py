def add(value1, value2):
    return value1 + value2


def subtract(value1, value2):
    return value1 - value2


def divide(value1, value2):
    return value1 / value2


def multiply(value1, value2):
    return value1 * value2


def calculate(operator, value1, value2):
    if operator == "+":
        print(add(value1, value2))
    elif operator == "-":
        print(subtract(value1, value2))
    elif operator == "/":
        print(divide(value1, value2))
    elif operator == "*":
        print(multiply(value1, value2))
    else:
        return False

    return True


while True:
    value1 = int(input("Digito 1 "))
    value2 = int(input("Digite 2 "))

    operator = input("+, -, / ou *? ")

    if not calculate(operator, value1, value2):
        break
