import json

class Employee:
    def __init__(self, id, start_date, department, salary):
        self.id = id
        self.start_date = start_date
        self.department = department
        self.salary = salary
    
    def __repr__(self):
        return "<Employee #%r, Dept: %r, Comp: %r, Started: %r >" % (self.id, self.department, self.salary, self.start_date)

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True)