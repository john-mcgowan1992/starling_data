"""
The vast majority of our app involves the user requesting some data that requires us to do some manipulation on the backend before returning it to the user. Imagine we have some simple datastructure with columns:

- Employee ID
- Salary
- Effectvie Date
- Department

Note that Employee ID is a unique identifier for the individual person. A person joins the company when their employee ID has its first effective date. If the same ID has multiple effective dates, that may be a result of getting a raise, or switching departments within the company. 

Assume that the company has no employees other than the ones in the data, and that no one leaves the company after they join.

Your task is to write a small backend server with two endpoints:

/averages
and
/headcount_over_time

The /averages endpoint should accept a GET request and return the *average current salary* of employees broken down by department, eg
{
  "Design": 64000,
  "Engineering": 70000
}

The /headcount_over_time endpoint should accept GET requests along with a possible parameter 'department'. It should return the headcount of the organization for each month, possibly filtered by the value of the 'department' parameter. It should return something like:
{
  "data": [
    {"month": "2015-05-01",
    "headcount": 5},
    {"month": "2015-06-01",
    "headcount": 6},
    ...
  ]
}

Please use python for this task, though feel free to use whichever librarys/frameworks  you like. As for the data, pretend the variable 'employee_data' is output from querying the database for all records.

The server should get up and running by just running this file with `python simple_api.py` from the command-line.

"""


employee_data = [
 {'date': '2017-03-01', 'dept': 'Sales', 'employee': 3, 'salary': 70000},
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

 formatted = {
  3: {'2017-03-01': ('Sales', 70000)}, 
  4: {'2015-03-01': ('Engineering', 45000), '2017-09-01': ('Sales', 60000)},
  5: {'2016-02-01': ('Support', 40000), '2017-12-01': ('Support', 65000), '2016-03-01': ('Sales', 40000)},
  6: {'2016-11-01': ('Engineering', 45000), '2016-03-01': ('Support', 70000)},
  7: {'2017-11-01': ('Support', 50000), '2015-08-01': ('Engineering', 65000), '2015-09-01': ('Sales', 55000), '2017-04-01': ('Engineering', 70000)},
  8: {'2015-08-01': ('Engineering', 60000)},
  9: {'2017-11-01': ('Sales', 55000), '2015-01-01': ('Support', 55000)}, 
  10: {'2017-12-01': ('Engineering', 55000), '2016-12-01': ('Sales', 50000), '2017-04-01': ('Engineering', 70000)}, 
  11: {'2016-11-01': ('Support', 75000)}, 
  12: {'2015-11-01': ('Support', 45000), '2016-06-01': ('Engineering', 40000), '2015-01-01': ('Sales', 40000), '2016-08-01': ('Sales', 40000)}, 
  13: {'2017-08-01': ('Engineering', 75000), '2015-01-01': ('Engineering', 70000), '2016-03-01': ('Sales', 60000)}, 
  14: {'2015-12-01': ('Sales', 60000)}, 
  16: {'2017-07-01': ('Support', 60000)}, 
  17: {'2016-12-01': ('Engineering', 45000)}, 
  18: {'2017-11-01': ('Engineering', 45000)}, 
  20: {'2015-03-01': ('Engineering', 45000)}, 
  21: {'2016-06-01': ('Sales', 40000), '2016-09-01': ('Engineering', 70000)}, 
  23: {'2016-02-01': ('Engineering', 75000), '2016-01-01': ('Engineering', 50000)}, 
  24: {'2017-04-01': ('Engineering', 55000)}, 
  25: {'2016-09-01': ('Engineering', 50000)},
  28: {'2017-05-01': ('Sales', 60000)}, 
  29: {'2017-10-01': ('Support', 40000)}, 
  30: {'2017-06-01': ('Engineering', 70000)}}

def run_api():
  print ":)"

if __name__ == '__main__':
  run_api()
