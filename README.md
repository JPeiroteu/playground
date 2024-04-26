# Clean Code Playground: grades.py and calculator.py

This project consists of two Python modules: `grades.py` and `calculator.py`, along with corresponding unit test files `test_calculator.py` and `test_grades.py`.

### calculator.py

The `calculator.py` module provides basic arithmetic operations such as addition, subtraction, multiplication, division, and square root. The calculations can be performed via both a command-line interface (CLI) and HTTP endpoints.

### grades.py
The `grades.py` module facilitates managing student grades. It includes a `Student` class for representing students and their assignments, as well as a `Work` class for individual assignments. This allows professors to add grades for them assignments, and the module calculates their final grades based on the weights assigned to each assignment.

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

## Running the Applications

### RPN Calculator

To run the RPN calculator, execute the following command:
```bash
python calculator.py
```
You can interact with the calculator via the command line or make HTTP requests to perform calculations (via Postman API Platform)

### Student Grades Management

To manage student grades, run the following command:
```bash
python grades.py
```
This tool provides a command-line interface for adding and calculating student grades.

## Usage Instructions

### RPN Calculator

#### CLI Usage:

1. **POST `/calculate` (Calculate):**
   - `curl -X POST http://localhost:8000/calculate -d "input=-"`

2. **POST `/number` (Add Number):**
   - `curl -X POST http://localhost:8000/number -d "value=5"`

3. **GET `/stack` (Get Stack):**
   - `curl http://localhost:8000/stack`

4. **POST `/reset` (Reset Stack):**
   - `curl -X POST http://localhost:8000/reset`

### Student Grades Management

#### CLI Usage:
- Follow the on-screen prompts to manage student grades interactively.

## Use Cases

### Calculator Module:
- **Interactive Command-Line Usage:**
  - Perform arithmetic operations interactively via CLI.
  - Use web endpoints for calculations and stack management.
  - Add numbers with `/number`, perform operations with `/calculate`, and view stack with `/stack`.

### Grades Module:
- **Interactive Command-Line Usage:**
  - Manage student grades interactively.
  - Input student names, assignments, grades, and weights.
- **Functionality:**
  - Add grades for assignments with specified weights.
  - Calculate final grades based on assignment weights.
  - Reset student data as needed.

## Code Analysis

The project's code quality has been assessed using Pylint, a popular tool for analyzing Python code and ensuring adherence to best practices and style guidelines.

### Summary of Code Quality Improvements

#### calculator.py

![calculator.py pylint feedback](https://github.com/JPeiroteu/playground/assets/79811891/be16b1a0-903d-40a6-922d-d9168667c7be)

To enhance the quality of `calculator.py`, the following improvements were made:

- Trailing whitespace was removed.
- A module docstring was added for better understanding of the code's purpose.
- Comments were added to clarify code functionality.
- Public methods were increased in certain classes for improved code organization.
- Variable `op` was renamed to adhere to snake_case convention for consistency.
- Return statements within functions were made consistent for better code readability.
- Import order of modules was corrected to follow Python conventions.
- An unused import was removed to declutter the codebase.

#### grade.py

![grade.py pylint feedback](https://github.com/JPeiroteu/playground/assets/79811891/1967e5a9-59a6-48ec-9368-8f75a3d3a97a)

Similar improvements were implemented in `grade.py`.

By running Pylint on both `calculator.py` and `grade.py`, we ensure that the code maintains high standards of readability, maintainability, and adherence to Python coding conventions.
