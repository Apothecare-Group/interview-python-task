# Graduate Python Developer Task Repository

This repository contains a Python project designed as a coding task for graduate-level Python developers. The task involves implementing a function to calculate the factorial of a given number. The repository also includes unit tests to validate the implementation.

## Coding Task

### Task Description

Write a Python function that takes a non-negative integer as input and returns its factorial. The factorial of a number `n` is the product of all positive integers less than or equal to `n`. For example, the factorial of 5 is `5! = 5 × 4 × 3 × 2 × 1 = 120`.

### Candidate Instructions

1. Implement the function by replacing the placeholder in the provided file with your solution.
2. Ensure your solution handles edge cases, such as `0! = 1`, and produces the correct output for all valid inputs.

## Project Structure

```
python-task-repo
├── src
│   ├── main.py
│   └── tests
│       └── test_main.py
├── requirements.txt
└── README.md
```

## Setup Instructions

1. **Clone the repository:**

   ```bash
   git clone <repository-url>
   cd python-task-repo
   ```

2. **Set up a virtual environment:**

   For Windows:

   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

   For macOS/Linux:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the main program:**

   You can run the main program to test your function:

   ```bash
   python src/main.py
   ```

5. **Run the tests:**

   To validate your implementation, run the unit tests using the following command:

   ```bash
   pytest src/tests/test_main.py
   ```

## Functionality

The main function `calculate_factorial` takes a non-negative integer as input and returns its factorial. The program includes sample inputs to demonstrate its functionality.