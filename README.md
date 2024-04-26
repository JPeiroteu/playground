# Clean Code Playground: grades.py and calculator.py

## Overview

This project consists of two Python modules: `grades.py` and `calculator.py`, along with a corresponding unit test file `test_calculator.py`.

### grades.py
The `grades.py` module facilitates managing student grades. It includes a `Student` class for representing students and their assignments, as well as a `Work` class for individual assignments. Students can add grades for their assignments, and the module calculates their final grades based on the weights assigned to each assignment.

### calculator.py
The `calculator.py` module provides basic arithmetic operations such as addition, subtraction, multiplication, division, and square root. The calculations can be performed via a command-line interface (CLI). It includes classes for different arithmetic operations and operates on a stack-based approach.

### test_calculator.py
The `test_calculator.py` file contains unit tests for the functionality implemented in the `calculator.py` module. It verifies the correctness of arithmetic operations and stack manipulation in the RPN calculator.

## Development Environment Setup

To set up the development environment, follow these steps:

1. Clone the repository:
   ```
   git clone https://github.com/JPeiroteu/playground.git
   ```

2. Navigate to the project directory:
   ```
   cd playground
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Running the Application

### Command-Line Calculator

To run the command-line calculator, execute the following command:
```
python calculator.py
```
Follow the on-screen prompts to perform calculations.

## Use Cases

- The command-line calculator allows users to perform arithmetic operations interactively.
- The web application exposes endpoints for performing calculations and managing a stack.
- Users can input numbers and operations via HTTP POST requests to the `/number` and `/calculate` endpoints, respectively.
- The current stack can be retrieved by sending a GET request to the `/stack` endpoint.

## Code Analysis

The project's code quality has been assessed using Pylint, a popular tool for analyzing Python code and ensuring adherence to best practices and style guidelines.

### Pylint Feedback

#### calculator.py

![calculator.py pylint feedback](https://github.com/JPeiroteu/playground/assets/79811891/be16b1a0-903d-40a6-922d-d9168667c7be)

#### grade.py

![grade.py pylint feedback](https://github.com/JPeiroteu/playground/assets/79811891/be16b1a0-903d-40a6-922d-d9168667c7be)

By running Pylint on both `calculator.py` and `grade.py`, we ensure that the code maintains high standards of readability, maintainability, and adherence to Python coding conventions.