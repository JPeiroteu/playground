"""
RPN Calculator
"""

import math
from flask import Flask, request

app = Flask(__name__)

class Operation:
    """Base class for operations."""
    def __init__(self, operator):
        self.operator = operator

class Addition(Operation):
    """Class for addition operation."""
    def operate(self, stack):
        return stack.pop() + stack.pop()

class Subtract(Operation):
    """Class for subtraction operation."""
    def operate(self, stack):
        return stack.pop() - stack.pop()

class Divide(Operation):
    """Class for division operation."""
    def operate(self, stack):
        denominator = stack.pop()
        return stack.pop() / denominator

class Multiply(Operation):
    """Class for multiplication operation."""
    def operate(self, stack):
        return stack.pop() * stack.pop()

class SquareRoot(Operation):
    """Class for square root operation."""
    def operate(self, stack):
        return math.sqrt(stack.pop())

class Stack:
    """Class representing the stack."""
    def __init__(self):
        self.stack = []
        self.operations = [
            Addition("+"),
            Subtract("-"),
            Divide("/"),
            Multiply("*"),
            SquareRoot("sqrt")
        ]

    def push(self, value):
        """Push value onto the stack."""
        self.stack.append(value)

    def pop(self):
        """Pop value from the stack."""
        return self.stack.pop()

    def calculate(self, operator):
        """Calculate result based on operator."""
        for operation in self.operations:
            if operation.operator == operator:
                return operation.operate(self.stack)

stack = Stack()

@app.route("/")
def welcome():
    """Welcome message."""
    return "<p>Welcome to RPN Calculator!</p>"

@app.route("/calculate", methods=["POST"])
def calculate():
    """Perform calculation."""
    operator = request.form['input']
    if operator in [op.operator for op in stack.operations]:
        stack.push(stack.calculate(operator))
    else:
        return "error: Invalid operation. Please try again."
    return {
        "stack": stack.stack
    }

@app.route("/number", methods=["POST"])
def number():
    """Push number onto the stack."""
    value = request.form['value']
    if value.isnumeric():
        stack.push(int(value))
    else:
        return "error: Invalid operation. Please try again."
    return {
        "stack": stack.stack
    }

@app.route("/stack")
def get_stack():
    """Get current stack."""
    return {
        "stack": stack.stack
    }

@app.route("/reset", methods=["POST"])
def reset():
    """Reset stack."""
    stack.stack = []
    return {
        "status": "stack reset"
    }, 200

if __name__ == "__main__":
    app.run(port=8000, debug=True)