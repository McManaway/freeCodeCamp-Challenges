# Arithmetic Formatter Challenge for freeCodeCamp Course
# "Scientific Computing with Python"
# Author: Blake McManaway
# GitHub: McManaway
# ------------------------------------------------------------------- #


def arithmetic_arranger(math_problems: list, answers=False) -> str:
    """
    Returns addition and subtraction problems formatted vertically.
    :param math_problems: A list of addition or subtraction problems.
           Each problem should be in quotes. Maximum number of
           problems is five (5).
    :param answers: A bool indicating whether to include answers in
           the display. Defaults to not showing answers.
    """
    # Function-specific parameters. Could be changed to accommodate
    # further use cases.
    max_list_size = 5
    acceptable_operations = "+-"
    max_digits = 4
    acceptable_digits = "0123456789"
    problem_spacing = "    "
    newline = "\n"
    arranged_final = ""

    # Check for max list size
    if len(math_problems) > max_list_size:
        return "Error: Too many problems."

    # Initialize loop variables
    numbers = []
    problem_length = []
    answer = ""
    answer_list = []

    # Loop through list of strings, separate digits and operators
    for problem in math_problems:
        problem_list = problem.split(" ")
        num_1 = problem_list[0]
        operator = problem_list[1]
        num_2 = problem_list[2]

        # Now that numbers and operators are parsed out, check for
        # max number size, unsupported operators, and non-numbers
        if len(num_1) > max_digits or len(num_2) > max_digits:
            return "Error: Numbers cannot be more than four digits."
        if operator not in acceptable_operations:
            return "Error: Operator must be '+' or '-'."
        for char in num_2 + num_1:
            if char not in acceptable_digits:
                return "Error: Numbers must only contain digits."

        # Generate list of tuples. Helpful in problem construction
        # because it allows us to select top numbers when printing
        # the top row and bottom numbers when printing the bottom row.
        numbers.append((num_1, operator, num_2))

        # If answers requested, calculate answers now.
        if answers:
            answer = str(eval(num_1 + operator + num_2))
            answer_list.append(answer)

        # Compare lengths of all items involved in constructing this
        # particular problem. This will dictate how many dashes are
        # printed and how far to the right to print each number.
        if len(answer) > len(num_2) and len(answer) > len(num_1):
            problem_length.append(len(answer) + 1)
        else:
            if len(num_1) > len(num_2):
                problem_length.append(len(num_1) + 2)
            else:
                problem_length.append(len(num_2) + 2)

    # PROBLEM CONSTRUCTION
    # Need to print 4 lines: top, bottom, dashes, answer
    # Top
    for i in range(len(numbers)):
        arranged_final += " "*(problem_length[i] - len(numbers[i][0]))
        arranged_final += f"{numbers[i][0]}"
        if i != len(numbers) - 1:
            arranged_final += problem_spacing
    arranged_final += newline

    # Bottom
    for i in range(len(numbers)):
        arranged_final += f"{numbers[i][1]}"
        num_spaces = problem_length[i] - len(numbers[i][2]) - 1
        arranged_final += " "*(num_spaces)
        arranged_final += f"{numbers[i][2]}"

        if i != len(numbers) - 1:
            arranged_final += problem_spacing
    arranged_final += newline

    # Dashes
    for i in range(len(problem_length)):
        arranged_final += "-"*problem_length[i]
        if i != len(problem_length) - 1:
            arranged_final += problem_spacing

    # Answers
    if answers:
        arranged_final += newline
        for i in range(len(numbers)):
            arranged_final += " "*(problem_length[i] - len(answer_list[i]))
            arranged_final += answer_list[i]
            if i != len(numbers) - 1:
                arranged_final += problem_spacing

    # If all checks pass:
    return arranged_final


# TESTING
# ------------------------------------------------------------------- #
# Test cases
# ------------------------------------------------------------------- #
# Simple, Error-Free
list1 = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
list2 = ["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"]
list3 = ["5 + 3", "29 + 323"]
# ------------------------------------------------------------------- #
# Too long, Error
list4 = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49", "50 + 67",
         "13 - 475"]
# Multiplication or Division, Error
list5 = ["5 * 3", "29 * 323"]
list6 = ["32 / 8", "1 / 3801", "9999 / 9999", "523 / 49"]
# Non-numeric, Error
list7 = ["150 + 9", "6x - 276y"]
list8 = ["15@ + 5!!", "6&&& - 276$"]
# Numbers over four digits, Error
list9 = ["324 + 869", "1 - 38017", "99999 + 9999", "52345 - 49"]
# ------------------------------------------------------------------- #
testcases = {"Error-Free": [list1, list2, list3],
             "List-Error": [list4],
             "Operator-Error": [list5, list6],
             "Digit-Error": [list7, list8],
             "Size-Error": [list9]
             }

# AUTOMATIC TESTING FUNCTION
# -------------------------------------------------------------------- #


def arranger_test(cases: dict) -> bool:
    index_tripped = []
    expected_result = ""
    for key, case_list in cases.items():
        for item in case_list:
            result1 = arithmetic_arranger(item, False)
            result2 = arithmetic_arranger(item, True)
            if key == "Error-Free":
                expected_result = ""
            if key == "List-Error":
                expected_result = "Error: Too many problems."
            if key == "Operator-Error":
                expected_result = "Error: Operator must be '+' or '-'."
            if key == "Digit-Error":
                expected_result = "Error: Numbers must only " \
                                  "contain digits."
            if key == "Size-Error":
                expected_result = "Error: Numbers cannot be more " \
                                  "than four digits."
            if expected_result != result1 or expected_result != result2:
                index_tripped.append(item)

    print("*"*40)

    if index_tripped:
        print(index_tripped)
        print("Test failed. The above problem set(s) caused an error.")
        return False

    print("All tests passed")
    return True
