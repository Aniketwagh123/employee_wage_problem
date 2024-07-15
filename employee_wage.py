import random

WAGE_PER_HOUR = 20
FULL_DAY_HOUR = 8
PART_TIME_HOUR = 4

def calculate_wage(hours):
    return hours * WAGE_PER_HOUR

def check_attendance():
    return random.choice(["full_time", "part_time", "absent"])

if __name__ == "__main__":
    print("Welcome to Employee Wage Computation Program")
    employee_type = check_attendance()
    if employee_type == "full_time":
        wage = calculate_wage(FULL_DAY_HOUR)
    elif employee_type == "part_time":
        wage = calculate_wage(PART_TIME_HOUR)
    else:
        wage = 0

    print(f"Employee Wage: {wage}")