# Utility functions for the Company and Employee classes

from datetime import datetime
from dateutil.relativedelta import relativedelta
from Employee import Employee

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

def department_headcount(company):
    headcount_list = list()
    start_date = datetime.strptime(company.date_founded, "%Y-%m-%d")
    emp_dict = company.employee_dictionary
    for i in range(36):
        month_dict = dict()
        current_month = start_date + relativedelta(months=+i)
        month_dict['month'] = datetime.strftime(current_month, "%Y-%m-%d")
        month_dict['chart_label'] = datetime.strftime(current_month, "%m-%y")
        month_dict['Engineering'] = 0
        month_dict['Sales'] = 0
        month_dict['Support'] = 0
        month_dict['Total'] = 0
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
                month_count['Total'] += 1
    return headcount_list