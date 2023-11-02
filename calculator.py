''' RPN Calculator '''
import math

class Operation:
    def __init__ (self, operator):
        self.operator = operator

    def operate (self, stack):
        pass


class Addition(Operation):
    def operate (self, stack):
        return stack.pop() + stack.pop()

class Subtract(Operation):
    def operate (self, stack):
        return stack.pop() - stack.pop()

class Divide(Operation):
    def operate (self, stack):
        denominator = stack.pop()
        return stack.pop() / denominator

class Multiply(Operation):
    def operate (self, stack):
        return stack.pop() * stack.pop()

class SquareRoot(Operation):
    def operate (self, stack):
        return math.sqrt(stack.pop())

class Stack:
    def __init__ (self):
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


stack = Stack() #object

while True:
    val_oper = input("> ")

    if val_oper.isnumeric():
        stack.push(int(val_oper))

    else:
        stack.push(stack.calculate(val_oper))

        """
        if not calculate(val_oper):
            break"""

    print(stack.stack)