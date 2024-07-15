import random

WAGE_PER_HOUR = 20
FULL_DAY_HOUR = 8


def check_attendance():
    return random.choice([True, False])


if __name__ == "__main__":
    print("Welcome to Employee Wage Computation Program")
    if check_attendance():
        daily_wage = WAGE_PER_HOUR * FULL_DAY_HOUR
        print(f"Daily Employee Wage: {daily_wage}")
    else:
        print("Employee is Absent")
