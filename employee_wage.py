import random

WAGE_PER_HOUR = 20
FULL_DAY_HOUR = 8
PART_TIME_HOUR = 4
MAX_HOURS_IN_MONTH = 100
MAX_DAYS_IN_MONTH = 20


def calculate_wage(hours):
    return hours * WAGE_PER_HOUR


def get_wage(employee_type):
    match employee_type:
        case 'full_time':
            return calculate_wage(FULL_DAY_HOUR)
        case 'part_time':
            return calculate_wage(PART_TIME_HOUR)
        case 'absent':
            return 0


if __name__ == "__main__":
    print("Welcome to Employee Wage Computation Program")
    total_hours = 0
    total_days = 0
    total_wage = 0

    while total_hours < MAX_HOURS_IN_MONTH and total_days < MAX_DAYS_IN_MONTH:
        employee_type = random.choice(['full_time', 'part_time', 'absent'])
        hours_worked = FULL_DAY_HOUR if employee_type == 'full_time' else PART_TIME_HOUR
        if employee_type != 'absent':
            total_hours += hours_worked
            total_wage += get_wage(employee_type)
        total_days += 1
    print(f"Total Wage for the Month: {total_wage}")