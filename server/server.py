from flask import Flask
from flask import request
from flask import Response
from flask import send_from_directory
from flask import render_template
from flask import jsonify
import os.path

from employees import EMPLOYEES, EMPLOYEES_FORMATTED

STATIC_RESOURCES = os.path.abspath("../client/public")
print EMPLOYEES

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
    salaries_dict = compute_avg(EMPLOYEES_FORMATTED)
    return jsonify(salaries_dict)

@app.route("/api/highest_earners")
def highest_earners():
    def compute_earners(employee_list):
        earners_desc = list()
        for department, employees in employee_list.iteritems():
            earners_desc.extend(employees)
        earners_desc.sort(key=lambda x: x.salary)
        return earners_desc
    earners = compute_earners(EMPLOYEES_FORMATTED)
    return jsonify(earners)
    
@app.route("/api/headcount_over_time/<string:department>")
def headcount(department):
    print department
    return jsonify({"dept": department})

@app.route("/api/headcount_total")
def total_headcount():
    total = EMPLOYEES.employee_count
    return jsonify({"total": total})