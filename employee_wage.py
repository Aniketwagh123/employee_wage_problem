import random

WAGE_PER_HOUR = 20
FULL_DAY_HOUR = 8
PART_TIME_HOUR = 4
WORKING_DAYS_PER_MONTH = 20


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
    total_wage = 0
    for day in range(WORKING_DAYS_PER_MONTH):
        employee_type = random.choice(['full_time', 'part_time', 'absent'])
        total_wage += get_wage(employee_type)
    print(f"Total Wage for the Month: {total_wage}")