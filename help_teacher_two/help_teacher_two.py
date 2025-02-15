"""
Constants used for grade calculations and student information.

Constants:
    NUMBER_ONE (int): The integer value 1, used for counting or indexing.
    NUMBER_TWO (int): The integer value 2, used for averaging or comparing two subjects.
    ZERO (int): The integer value 0, used as an initial value for counters or sums.
    NUMBER_ONE_HUNDRED_ONE (int): The integer value 101, can be used for specific grade thresholds or limits.
    FAILED_GRADE (int): The grade threshold below which a student is considered to have failed (default is 55).
    SUBJECT_ENGLISH (str): The string key representing the English subject.
    SUBJECT_MATH (str): The string key representing the Math subject.
    STUDENT_NAME (str): The string key representing the name of the student.

"""

NUMBER_ONE = 1
NUMBER_TWO = 2
ZERO = 0
NUMBER_ONE_HUNDRED_ONE = 101
FAILED_GRADE = 55
SUBJECT_ENGLISH = "English"
SUBJECT_MATH = "Math"
STUDENT_NAME = "Name"


def user_input(input_message: str,
               is_integer: bool):
    """
    Get user input and convert it to the desired type.

    Parameters:
    input_message (str): The message to display to the user.
    is_integer (bool): True if the input should be converted
                       to an integer, False for float.

    Returns:
    int or float: The user input converted to the specified type.
    """
    return int(input(input_message)) if is_integer \
        else float(input(input_message))


def get_student_name() -> str:
    """
    Prompt the user for a student's name.

    Returns:
    str: The name of the student entered by the user.
    """
    return input("Enter student name: ")


def get_best_grade(english: int,
                   math: int) -> int:
    """
    Determine the best grade between English and Math.

    Parameters:
    english (int): The English grade.
    math (int): The Math grade.

    Returns:
    int: The higher of the two grades.
    """
    return english if english > math else math


def get_average(english: int,
                math: int) -> float:
    """
    Calculate the average of the English and Math grades.

    Parameters:
    english (int): The English grade.
    math (int): The Math grade.

    Returns:
    float: The average grade.
    """
    return (english + math) / NUMBER_TWO


def print_student_info(list_students: list[dict]) -> None:
    """
    Print the information of each student in the list.

    Parameters:
        list_students (list[dict]): A list of dictionaries
                                    containing student information.
    """
    print("\nStudent Information: ")

    for val in list_students:
        print(f"\nStudent: {val[STUDENT_NAME]}, "
              f"Best Grade: {get_best_grade(val[SUBJECT_ENGLISH], val[SUBJECT_MATH])}, "
              f"Average Grade: {get_average(val[SUBJECT_ENGLISH], val[SUBJECT_MATH])}")


def get_grade(subject: str) -> float:
    """
    Prompt the user for a grade in the specified subject and validate it.

    Parameters:
    subject (str): The subject for which to get the grade (e.g., 'English' or 'Math').

    Returns:
    float: The validated grade entered by the user.
    """
    input_subject = ""
    while True:
        try:
            if subject == "English":
                input_subject = (
                    user_input("Enter English grade: ",
                               False))
            if subject == "Math":
                input_subject = (
                    user_input("Enter Math grade: ",
                               False))
            if not (NUMBER_ONE < input_subject < NUMBER_ONE_HUNDRED_ONE):
                raise ValueError()
        except ValueError:
            print("Expected a number")
        else:
            break
    return input_subject


def create_student_details(student_name: str,
                           subject_english: float,
                           subject_math: float) -> dict:
    """
    Create a dictionary with student details.

    Parameters:
    student_name (str): The name of the student.
    subject_english (float): The English grade.
    subject_math (float): The Math grade.

    Returns:
    dict: A dictionary containing the student's name and grades.
    """
    return {STUDENT_NAME: student_name, SUBJECT_ENGLISH: subject_english,
            SUBJECT_MATH: subject_math}


def get_student_info() -> dict:
    """
    Collect and return student information.

    Returns:
    dict: A dictionary containing the student's name and
          grades for English and Math.
    """
    return create_student_details(get_student_name(),
                                  get_grade(SUBJECT_ENGLISH),
                                  get_grade(SUBJECT_MATH))


def display_student_details(number: int) -> None:
    """
    Display a message indicating which student's details are being entered.

    Parameters:
    number (int): The student number.
    """
    print(f"Enter details for student {number}:")


def get_number_of_students() -> int:
    """
    Prompt the user for the number of students and validate the input.

    Returns:
    int: The number of students.

    Raises:
    ValueError: If the input is not a positive integer.
    """
    while True:
        try:
            input_number_students = user_input(
                "Enter the number of students: ", True)

            if input_number_students < NUMBER_ONE:
                raise ValueError()
        except ValueError:
            print("Expected a positive integer")
        else:
            break
    return input_number_students


def iterate_students_list(number_students: int) -> list[dict]:
    """
    Iterate through the number of students and gather their information.

    Parameters:
    number_students (int): The number of students.

    Returns:
    list[dict]: A list of dictionaries containing the details of each student.
    """
    list_students = []

    for number in range(1, number_students + NUMBER_ONE):
        display_student_details(number)
        list_students.append(get_student_info())

    return list_students


def get_average_grades_per_subject(english_average: float,
                                   math_average: float,
                                   number_students: int) -> dict:
    """
    Calculates the average grade per student for each subject.

    Parameters:
        english_average (float): The total average grade for the English subject.
        math_average (float): The total average grade for the Math subject.
        number_students (int): The number of students across all subjects.

    Returns:
        dict: A dictionary containing the per-student average grades for English
              and Math, with the subjects as keys and the averages as values.
              Example: {'English': 85.5, 'Math': 90.3}

    """
    return {SUBJECT_ENGLISH: english_average / number_students,
            SUBJECT_MATH: math_average / number_students}


def get_overall_average_grade(average_grades_per_subject: dict) -> float:
    """
    Calculates the overall average grade across all subjects.

    Parameter:
        average_grades_per_subject (dict): A dictionary containing the per-student
                                           average grades for each subject, where
                                           the keys are the subject names and
                                           the values are the average grades.

    Returns:
        float: The overall average grade across the subjects.
    """
    return (average_grades_per_subject[SUBJECT_ENGLISH] +
            average_grades_per_subject[SUBJECT_MATH]) / NUMBER_TWO


def calculate_average_grades(students: list[dict]) -> tuple:
    """
    Calculates the average grades for each subject and the overall average grade.

    Parameter:
        students (list[dict]): A list of dictionaries where each dictionary represents
                               a student, with keys for each subject ('English' and 'Math')
                               and values representing the grades for those subjects.

    Returns:
        tuple: A tuple where:
            - The first element is a dictionary with the per-student average grades
              for each subject.
            - The second element is the overall average grade across all subjects.

    Example: ({'English': 85.5, 'Math': 90.3}, 87.9)

    """
    math_average = ZERO
    english_average = ZERO

    for student in students:
        english_average += student[SUBJECT_ENGLISH]
        math_average += student[SUBJECT_MATH]

    average_grades_per_subject = (get_average_grades_per_subject
                                  (english_average, math_average,
                                   len(students)))

    return (average_grades_per_subject,
            get_overall_average_grade(average_grades_per_subject))


def calculate_failing_grades(students: list[dict]) -> tuple:
    """
     Calculates the number of failing grades for each student and the total failing grades.

     Parameter:
         students (list[dict]): A list of dictionaries representing individual students. Each
                                dictionary contains:
                                - 'English' and 'Math' keys with their respective grades.
                                - 'Student Name' key for identifying the student.

     Returns:
         tuple: A tuple where:
             - The first element is a dictionary containing the number of failing grades per
               student. The keys are the student names, and the values are the number of subjects
               in which the student failed.
             - The second element is an integer representing the total number of failing grades
               across all students.

    Example: ({'John Doe': 1, 'Jane Doe': 0}, 1)

     """
    failing_grades_information = {}
    failing_grades_total = ZERO
    failed_count = ZERO

    for student in students:
        if student[SUBJECT_ENGLISH] <= FAILED_GRADE:
            failed_count += 1
        if student[SUBJECT_MATH] <= FAILED_GRADE:
            failed_count += 1
        failing_grades_information[student[STUDENT_NAME]] = failed_count
        failing_grades_total += failed_count
        failed_count = ZERO

    return failing_grades_information, failing_grades_total


def main() -> None:
    """
    Main function to manage student grade processing and output results.

    This function serves as the entry point for processing student grades. It:
    1. Retrieves the number of students and gathers the student data.
    2. Prints detailed information about each student.
    3. Calculates and prints the average grades for each subject, as well as the overall average grade.
    4. Calculates and prints the number of failing grades per student and the total failing grades.

    Returns:
        None: This function only prints output; it does not return any values.
    """
    number_students = get_number_of_students()
    students = iterate_students_list(number_students)

    print_student_info(students)

    (average_grades_per_subject,
     overall_average_grade) = calculate_average_grades(students)

    print("\nAverage grades per subject:")

    for subject, average_grade in average_grades_per_subject.items():
        print(f"{subject}: {average_grade:.2f}")

    print(f"\nOverall average grade across all subjects: "
          f"{overall_average_grade:.2f}")

    (failing_grades_information,
     total_failing_grades_for_all) = calculate_failing_grades(students)

    print("\nFailing grades per student:")

    for student_name, failed_grade_count in failing_grades_information.items():
        print(f"{student_name}: {failed_grade_count} failing grade(s)")

    print(f"\nTotal number of failing grades across all students: "
          f"{total_failing_grades_for_all}")


if __name__ == '__main__':
    main()
