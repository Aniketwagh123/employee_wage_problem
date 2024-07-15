import random

WAGE_PER_HOUR = 20
FULL_DAY_HOUR = 8
PART_TIME_HOUR = 4


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
    employee_type = random.choice(['full_time', 'part_time', 'absent'])
    print(f"Employee Wage: {get_wage(employee_type)}")
