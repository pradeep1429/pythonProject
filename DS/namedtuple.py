from collections import namedtuple
employee = namedtuple("Employee","name id type")
resource = employee(name = "pradeep", id = 555593, type = "fulltime")
print(resource.name)
employee.type = "parttime"
print(resource)
print(resource._asdict())