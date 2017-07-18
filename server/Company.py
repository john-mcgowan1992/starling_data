from employee_utils import format_list, current_employee_stats

class Company:
    def __init__(self, name, emp_list):
        self.name = name
        self.employee_dictionary = format_list(emp_list)
        self.employee_count = len(self.employee_dictionary)
        self.date_founded = min([emp['date'] for emp in emp_list])
        self.current_employees = current_employee_stats(self.employee_dictionary)
    
    def __repr__(self):
        return "<Company: %r, employees: %r, founded: %r >" % (self.name, self.employee_count, self.date_founded)