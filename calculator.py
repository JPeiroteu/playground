from flask import Flask, request
import math

app = Flask(__name__)

class Operation:
    def __init__(self, operator):
        self.operator = operator

class Addition(Operation):
    def operate(self, stack):
        return stack.pop() + stack.pop()

class Subtract(Operation):
    def operate(self, stack):
        second_operand = stack.pop()
        first_operand = stack.pop()
        return first_operand - second_operand

class Divide(Operation):
    def operate(self, stack):
        denominator = stack.pop()
        return stack.pop() / denominator

class Multiply(Operation):
    def operate(self, stack):
        return stack.pop() * stack.pop()

class SquareRoot(Operation):
    def operate(self, stack):
        return math.sqrt(stack.pop())

class Stack:
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
        self.stack.append(value)

    def pop(self):
        return self.stack.pop()

    def calculate(self, operator):
        for op in self.operations:
            if op.operator == operator:
                return op.operate(self.stack)

stack = Stack()


@app.route("/")
def welcome():
    return "<p>Welcome to RPN Calculator!</p>"

@app.route("/calculate", methods=["POST"])
def calculate():
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
    return {
        "stack": stack.stack
    }

@app.route("/reset", methods=["POST"])
def reset():
    stack.stack = [] 
    return {
        "status": "stack reset"
    }, 200

def tearDown(self):
    self.client.get('/reset')


if __name__ == "__main__":
    app.run(port=8000, debug=True)