import random


def check_attendance():
    return random.choice([True, False])


if __name__ == "__main__":
    print("Welcome to Employee Wage Computation Program")
    if check_attendance():
        print("Employee is Present")
    else:
        print("Employee is Absent")
