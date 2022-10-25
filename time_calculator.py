# Time Calculator Challenge for freeCodeCamp Course
# "Scientific Computing with Python"
# Author: Blake McManaway
# GitHub: McManaway

# Notable constraints: Do not import any Python libraries.
# Assume that the start times are valid times.
# The minutes in the duration time will be a whole number less than 60,
# but the hour can be any whole number.
# ------------------------------------------------------------------- #


def add_time(start_time: str, duration: str, starting_day="") -> str:
    """
    Adds duration to start time and returns an end time after the
    duration. If applicable, it will include how many days later. If
    a start day is inputted, it will return the end day.

    :param start_time: A string in the form "HH:MM AM/PM".
    :param duration: A string in the form "H:M".
    :param starting_day: Defaults to "".
    :return: A string indicating the end time/day.
    """
    # In general, this function is a simple "start + duration = end"
    # with two looping sets of numbers: hour 0-24, second 0-60

    # Initialize potential interim-math variables
    days_later = 0
    days_of_the_week = ["monday", "tuesday", "wednesday", "thursday",
                        "friday", "saturday", "sunday"]

    # Initialize end time variables
    e_hour = 0
    e_minute = 0
    e_time = 0
    e_meridian = ""
    e_day = ""

    # Parse start time
    s_day = starting_day.lower()
    s_time, s_meridian = start_time.split(" ")
    s_hour_str, s_minute_str = s_time.split(":")
    s_hour = int(s_hour_str)
    s_minute = int(s_minute_str)

    # Convert to 24-hour clock, for easier math
    if s_meridian == "PM":
        s_hour += 12

    # Parse duration
    d_hour_str, d_minute_str = duration.split(":")
    d_hour = int(d_hour_str)
    d_minute = int(d_minute_str)

    # Calculate end minute and end hour
    e_hour = s_hour + d_hour
    e_minute = s_minute + d_minute
    if e_minute > 59:
        e_minute -= 60
        e_hour += 1

    # Calculate days later and adjust hour
    # N days later is N factors of 24 above e_hour=24
    if e_hour > 24:
        days_later = e_hour // 24
        e_hour = e_hour % 24

    # Format the return time string
    if e_hour > 12:
        e_hour -= 12
        e_meridian = "PM"
    elif e_hour == 12:
        e_meridian = "PM"
    else:
        e_meridian = "AM"

    # Because we don't use 0 hour for some reason
    if e_hour == 0:
        e_hour = 12

    e_time = f"{str(e_hour)}:{e_minute:02} {e_meridian}"

    # Add day of the week if applicable
    if starting_day:
        day_index = days_of_the_week.index(s_day)
        effective_days = days_later % 7
        new_day_index = day_index + effective_days

        while new_day_index >= 7:
            new_day_index -= 7

        e_day = days_of_the_week[new_day_index]

        e_time += f", {e_day.capitalize()}"

    # Add days if applicable
    if days_later == 1:
        e_time += " (next day)"
    elif days_later > 1:
        e_time += f" ({days_later} days later)"
    print("Final answer: ", e_time)
    return e_time


# TESTING
# -------------------------------------------------------------------- #
# Test Cases
case1 = add_time("3:00 PM", "3:10")
case2 = add_time("11:30 AM", "2:32", "Monday")
case3 = add_time("11:43 AM", "00:20")
case4 = add_time("10:10 PM", "3:30")
case5 = add_time("11:43 PM", "24:20", "tueSday")
case6 = add_time("6:30 PM", "205:12")

exp_res1 = "6:10 PM"
exp_res2 = "2:02 PM, Monday"
exp_res3 = "12:03 PM"
exp_res4 = "1:40 AM (next day)"
exp_res5 = "12:03 AM, Thursday (2 days later)"
exp_res6 = "7:42 AM (9 days later)"

testcases = [
    (case1, exp_res1),
    (case2, exp_res2),
    (case3, exp_res3),
    (case4, exp_res4),
    (case5, exp_res5),
    (case6, exp_res6)
]


# AUTOMATIC TESTING SCRIPT
# -------------------------------------------------------------------- #
def add_time_test(cases: list) -> bool:
    for case in cases:
        if case[0] != case[1]:
            print(f"Error: {case} failed test.")
            return False

    print("All tests passed.")
    return True


# -------------------------------------------------------------------- #
