import random

class EmployeeWage:
    def __init__(self, wage_per_hour, max_hours_in_month, max_days_in_month):
        self.WAGE_PER_HOUR = wage_per_hour
        self.FULL_DAY_HOUR = 8
        self.PART_TIME_HOUR = 4
        self.MAX_HOURS_IN_MONTH = max_hours_in_month
        self.MAX_DAYS_IN_MONTH = max_days_in_month
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
        if  self.total_hours + hours_worked <= self.MAX_HOURS_IN_MONTH and self.total_days + 1 <= self.MAX_DAYS_IN_MONTH:
            self.total_hours += hours_worked
            self.total_wage += self.get_wage(employee_type)
            self.total_days += 1

    def get_total_wage(self):
        return self.total_wage

    def check_attendance(self):
        return random.choice(['full_time', 'part_time', 'absent'])

if __name__ == "__main__":
    print("Welcome to Employee Wage Computation Program")
    companies = [
        {"name": "Company A", "wage_per_hour": 20, "max_hours_in_month": 100, "max_days_in_month": 20},
        {"name": "Company B", "wage_per_hour": 25, "max_hours_in_month": 120, "max_days_in_month": 22}
    ]

    for company in companies:
        print(f"\nCalculating wages for {company['name']}")
        employee = EmployeeWage(company['wage_per_hour'], company['max_hours_in_month'], company['max_days_in_month'])
        while employee.total_hours < employee.MAX_HOURS_IN_MONTH and employee.total_days < employee.MAX_DAYS_IN_MONTH:
            employee_type = employee.check_attendance()
            employee.add_wage(employee_type)
        print(f"Total Wage for the Month for {company['name']}: {employee.get_total_wage()}")