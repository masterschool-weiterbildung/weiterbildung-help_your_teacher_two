# Student Grade Calculator

## Description
This project provides a Python script for managing student grades. It allows users to input student names, enter grades for English and Math, calculate averages, determine the highest grade, and identify failing students.

## Features
- Define constants for grade calculations.
- Input and validate student grades.
- Calculate individual and overall averages.
- Determine the highest grade in English and Math.
- Identify and count failing grades.
- Display student information in a structured format.

## Constants
The script uses the following constants:
- `NUMBER_ONE`, `NUMBER_TWO`, `ZERO`: Numeric values for calculations.
- `NUMBER_ONE_HUNDRED_ONE`: Upper limit for grades.
- `FAILED_GRADE`: Threshold for failing a subject (default is 55).
- `SUBJECT_ENGLISH`, `SUBJECT_MATH`, `STUDENT_NAME`: Keys for student information.

## Functions Overview
### User Input Functions
- `user_input(input_message, is_integer)`: Gets user input and converts it to integer or float.
- `get_student_name()`: Prompts user for a student name.

### Grade Calculation Functions
- `get_best_grade(english, math)`: Determines the highest grade between the two subjects.
- `get_average(english, math)`: Computes the average of English and Math grades.
- `get_average_grades_per_subject(english_avg, math_avg, num_students)`: Computes per-subject averages.
- `get_overall_average_grade(average_grades_per_subject)`: Computes the overall average.

### Student Information Processing
- `create_student_details(name, english, math)`: Creates a dictionary for student details.
- `print_student_info(list_students)`: Prints student details including grades and averages.
- `get_student_info()`: Collects and returns student details.
- `iterate_students_list(number_students)`: Iterates over students to collect data.
- `calculate_average_grades(students)`: Computes subject-wise and overall averages.
- `calculate_failing_grades(students)`: Determines students who failed and counts failing grades.

### Main Execution
- `main()`: Runs the complete process: collecting student data, calculating grades, and displaying results.

## How to Run
1. Ensure you have Python installed (Python 3 recommended).
2. Save the script as `student_grades.py`.
3. Open a terminal and navigate to the script directory.
4. Run the script:
   ```sh
   python student_grades.py
   ```
5. Follow the prompts to enter student details and view results.

## Example Output
```
Enter the number of students: 2
Enter details for student 1:
Enter student name: John
Enter English grade: 85
Enter Math grade: 90
Enter details for student 2:
Enter student name: Jane
Enter English grade: 78
Enter Math grade: 60

Student Information:

Student: John, Best Grade: 90, Average Grade: 87.5
Student: Jane, Best Grade: 78, Average Grade: 69.0

Average grades per subject:
English: 81.50
Math: 75.00

Overall average grade across all subjects: 78.25

Failing grades per student:
Jane: 1 failing grade(s)

Total number of failing grades across all students: 1
```
