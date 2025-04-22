# Python Test Repository

This repository contains a simple Python project that includes a function to filter even numbers from a list. It also includes unit tests to verify the correctness of the function.

## Coding Task

### Task Description

Write a Python function that takes a list of integers as input and returns a new list that contains only the even numbers from the original list.

### Candidate Instructions

1. Complete the function by replacing the placeholder with your solution.
2. Ensure your solution correctly handles the input and produces the expected output.

## Project Structure

```
python-test-repo
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
   cd python-test-repo
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

   You can run the main program to see the function in action:

   ```bash
   python src/main.py
   ```

5. **Run the tests:**

   To run the unit tests, use the following command:

   ```bash
   pytest src/tests/test_main.py
   ```

## Functionality

The main function `get_even_numbers` takes a list of integers as input and returns a list containing only the even numbers. The program includes a sample input to demonstrate its functionality.