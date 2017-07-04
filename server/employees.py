from datetime import datetime
from dateutil.relativedelta import relativedelta

raw_data = [{'date': '2017-03-01', 'dept': 'Sales', 'employee': 3, 'salary': 70000},
 {'date': '2015-03-01', 'dept': 'Engineering', 'employee': 4, 'salary': 45000},
 {'date': '2017-09-01', 'dept': 'Sales', 'employee': 4, 'salary': 60000},
 {'date': '2016-03-01', 'dept': 'Sales', 'employee': 5, 'salary': 40000},
 {'date': '2017-12-01', 'dept': 'Support', 'employee': 5, 'salary': 65000},
 {'date': '2016-02-01', 'dept': 'Support', 'employee': 5, 'salary': 40000},
 {'date': '2016-03-01', 'dept': 'Support', 'employee': 6, 'salary': 70000},
 {'date': '2016-11-01', 'dept': 'Engineering', 'employee': 6, 'salary': 45000},
 {'date': '2017-04-01', 'dept': 'Engineering', 'employee': 7, 'salary': 70000},
 {'date': '2015-09-01', 'dept': 'Sales', 'employee': 7, 'salary': 55000},
 {'date': '2017-11-01', 'dept': 'Support', 'employee': 7, 'salary': 50000},
 {'date': '2015-08-01', 'dept': 'Engineering', 'employee': 7, 'salary': 65000},
 {'date': '2015-08-01', 'dept': 'Engineering', 'employee': 8, 'salary': 60000},
 {'date': '2017-11-01', 'dept': 'Sales', 'employee': 9, 'salary': 55000},
 {'date': '2015-01-01', 'dept': 'Support', 'employee': 9, 'salary': 55000},
 {'date': '2017-12-01', 'dept': 'Engineering', 'employee': 10, 'salary': 55000},
 {'date': '2016-12-01', 'dept': 'Sales', 'employee': 10, 'salary': 50000},
 {'date': '2017-04-01', 'dept': 'Engineering', 'employee': 10, 'salary': 70000},
 {'date': '2016-11-01', 'dept': 'Support', 'employee': 11, 'salary': 75000},
 {'date': '2016-08-01', 'dept': 'Sales', 'employee': 12, 'salary': 40000},
 {'date': '2016-06-01', 'dept': 'Engineering', 'employee': 12, 'salary': 40000},
 {'date': '2015-01-01', 'dept': 'Sales', 'employee': 12, 'salary': 40000},
 {'date': '2015-11-01', 'dept': 'Support', 'employee': 12, 'salary': 45000},
 {'date': '2016-03-01', 'dept': 'Sales', 'employee': 13, 'salary': 60000},
 {'date': '2015-01-01', 'dept': 'Engineering', 'employee': 13, 'salary': 70000},
 {'date': '2017-08-01', 'dept': 'Engineering', 'employee': 13, 'salary': 75000},
 {'date': '2015-12-01', 'dept': 'Sales', 'employee': 14, 'salary': 60000},
 {'date': '2017-07-01', 'dept': 'Support', 'employee': 16, 'salary': 60000},
 {'date': '2016-12-01', 'dept': 'Engineering', 'employee': 17, 'salary': 45000},
 {'date': '2017-11-01', 'dept': 'Engineering', 'employee': 18, 'salary': 45000},
 {'date': '2015-03-01', 'dept': 'Engineering', 'employee': 20, 'salary': 45000},
 {'date': '2016-06-01', 'dept': 'Sales', 'employee': 21, 'salary': 40000},
 {'date': '2016-09-01', 'dept': 'Engineering', 'employee': 21, 'salary': 70000},
 {'date': '2016-01-01', 'dept': 'Engineering', 'employee': 23, 'salary': 50000},
 {'date': '2016-02-01', 'dept': 'Engineering', 'employee': 23, 'salary': 75000},
 {'date': '2017-04-01', 'dept': 'Engineering', 'employee': 24, 'salary': 55000},
 {'date': '2016-09-01', 'dept': 'Engineering', 'employee': 25, 'salary': 50000},
 {'date': '2017-05-01', 'dept': 'Sales', 'employee': 28, 'salary': 60000},
 {'date': '2017-10-01', 'dept': 'Support', 'employee': 29, 'salary': 40000},
 {'date': '2017-06-01', 'dept': 'Engineering', 'employee': 30, 'salary': 70000}]

def format_list(employee_list):
    list_cleaned = {}
    for entry in employee_list:
        new_entry = (entry["dept"], entry["salary"])
        key = entry["employee"]
        date_sub_key = entry["date"]
        if not key in list_cleaned:
            list_cleaned[key] = {}
            list_cleaned[key][date_sub_key] = new_entry
        else:
            list_cleaned[key][date_sub_key] = new_entry
    return list_cleaned

def return_current_employee(empID, empObj):
    empStartDates = list(empObj.keys())
    if len(empStartDates) == 1:
        emp = empObj[empStartDates[0]]
        emp_record = (empID, empStartDates[0], emp[0], emp[1])
        employee = Employee(*emp_record)
        return employee
    else:
        latest = max(dt for dt in empStartDates)
        emp = empObj[latest]
        emp_record = (empID, latest, emp[0], emp[1])
        employee = Employee(*emp_record)
        return employee

def current_employee_stats(employee_dict):
    employees_dept = {}
    for employeeID in employee_dict:
        new_emp = return_current_employee(employeeID, employee_dict[employeeID])
        if not new_emp.department in employees_dept:
            employees_dept[new_emp.department] = list()
            employees_dept[new_emp.department].append(new_emp)
        else:
            employees_dept[new_emp.department].append(new_emp)
    return employees_dept
        
class Company:
    def __init__(self, name, list):
        self.name = name
        self.employee_dictionary = format_list(list)
        self.employee_count = len(self.employee_dictionary)
        self.date_founded = min([emp['date'] for emp in list])
    
    def __repr__(self):
        return "<Company: %r, employees: %r, founded: %r >" % (self.name, self.employee_count, self.date_founded)

class Employee:
    def __init__(self, id, start_date, department, salary):
        self.id = id
        self.start_date = start_date
        self.department = department
        self.salary = salary
    
    def __repr__(self):
        return "<Employee #%r, Dept: %r, Comp: %r, Started: %r >" % (self.id, self.department, self.salary, self.start_date)

EMPLOYEES = Company("Starling", raw_data)
EMPLOYEES_FORMATTED = current_employee_stats(EMPLOYEES.employee_dictionary)
print EMPLOYEES

def department_headcount(company):
    headcount_list = list()
    start_date = datetime.strptime(company.date_founded, "%Y-%m-%d")
    emp_dict = company.employee_dictionary
    for i in range(36):
        month_dict = dict()
        current_month = start_date + relativedelta(months=+i)
        month_dict['month'] = datetime.strftime(current_month, "%Y-%m-%d")
        month_dict['Engineering'] = 0
        month_dict['Sales'] = 0
        month_dict['Support'] = 0
        headcount_list.append(month_dict)
    for month_count in headcount_list:
        current = month_count['month']
        for emp_id in company.employee_dictionary:
            employee_dates = list(company.employee_dictionary[emp_id].keys())
            relevant_dates = [dt for dt in employee_dates if dt <= current]
            if relevant_dates:
                current_position_start = max(relevant_dates)
                dept = company.employee_dictionary[emp_id][current_position_start][0]
                month_count[dept] += 1
    return headcount_list

print department_headcount(EMPLOYEES)