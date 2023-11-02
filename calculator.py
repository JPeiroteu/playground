''' RPN Calculator '''

class Calculator:
    def __init__ (self):
        self.stack = []

    def push(self, value):
        self.stack.append(value) 


    def pop(self):
        return self.stack.pop()  


    def add(self):
        return self.pop() + self.pop()


    def subtract(self):
        return self.pop() - self.pop()


    def divide(self):
        denominator = self.pop()
        return self.pop() / denominator


    def multiply(self):
        return self.pop() * self.pop()


    def calculate(self, operator):
        if operator == "+":
            return self.add()
        elif operator == "-":
            return self.subtract()
        elif operator == "/":
            return self.divide()
        elif operator == "*":
            return self.multiply()

calculator = Calculator() #object

while True:
    val_oper = input("Digit or + - / * ")

    if val_oper.isnumeric():
        calculator.push(int(val_oper))

    else:
        calculator.push(calculator.calculate(val_oper))

        """
        if not calculate(val_oper):
            break"""

    print(calculator.stack)