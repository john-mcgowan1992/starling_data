from flask import Flask
from flask import request
from flask import Response
from flask import send_from_directory
from flask import render_template
from flask import jsonify
import os.path
from employee_utils import department_headcount

# from employees import EMPLOYEES
from Company import Company
from raw_data import raw_data

EMPLOYEES = Company('Starling', raw_data)
STATIC_RESOURCES = os.path.abspath("../client/public")

app = Flask(__name__, template_folder=STATIC_RESOURCES)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/public/<path:filepath>")
def publicResources(filepath):
    return send_from_directory(STATIC_RESOURCES, filepath)

@app.route("/api/averages")
def average_salaries():
    def compute_avg(employee_list):
        averages = dict()
        for department, employees in employee_list.iteritems():
            salaries = [emp.salary for emp in employees]
            averages[department] = sum(salaries)/len(salaries)
        print averages
        return averages
    salaries_dict = compute_avg(EMPLOYEES.current_employees)
    return jsonify(salaries_dict)

@app.route("/api/highest_earners")
def highest_earners():
    def compute_earners(employee_list):
        earners_desc = list()
        for department, employees in employee_list.iteritems():
            earners_desc.extend(employees)
        earners_desc.sort(key=lambda x: x.salary, reverse=True)
        earners_json = [emp.to_json() for emp in earners_desc]
        return earners_json[:10]
    earners = compute_earners(EMPLOYEES.current_employees)
    return jsonify(earners)
    
@app.route("/api/headcount_over_time")
def headcount():
    company_headcount = department_headcount(EMPLOYEES)
    return jsonify(company_headcount)

@app.route("/api/headcount_total")
def total_headcount():
    total = EMPLOYEES.employee_count
    return jsonify({"total": total})