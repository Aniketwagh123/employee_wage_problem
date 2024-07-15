import random

class EmployeeWage:
    WAGE_PER_HOUR = 20
    FULL_DAY_HOUR = 8
    PART_TIME_HOUR = 4
    MAX_HOURS_IN_MONTH = 100
    MAX_DAYS_IN_MONTH = 20

    def __init__(self):
        self.total_wage = 0
        self.total_hours = 0
        self.total_days = 0

    def calculate_wage(self, hours):
        return hours * self.WAGE_PER_HOUR

    def get_wage(self, employee_type):
        match employee_type:
            case 'full_time':
                return self.calculate_wage(self.FULL_DAY_HOUR)
            case 'part_time':
                return self.calculate_wage(self.PART_TIME_HOUR)
            case 'absent':
                return 0

    def add_wage(self, employee_type):
        hours_worked = self.FULL_DAY_HOUR if employee_type == 'full_time' else self.PART_TIME_HOUR
        if self.total_hours + hours_worked <= self.MAX_HOURS_IN_MONTH and self.total_days + 1 <= self.MAX_DAYS_IN_MONTH:
            self.total_hours += hours_worked
            self.total_wage += self.get_wage(employee_type)
            self.total_days += 1

    def get_total_wage(self):
        return self.total_wage

    def check_attendance(self):
        return random.choice(['full_time', 'part_time', 'absent'])

if __name__ == "__main__":
    print("Welcome to Employee Wage Computation Program")
    employee = EmployeeWage()
    while employee.total_hours < EmployeeWage.MAX_HOURS_IN_MONTH and employee.total_days < EmployeeWage.MAX_DAYS_IN_MONTH:
        employee_type = employee.check_attendance()
        employee.add_wage(employee_type)
    print(f"Total Wage for the Month: {employee.get_total_wage()}")