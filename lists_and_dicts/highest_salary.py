"""
Problem:
Find the employee with the highest salary from a list of dictionaries.

Approach:

1. We have a list of people (employees) with their details
2. We want to find the one with the highest salary
3. Use Python's built-in `max()` function
4. Tell `max()` HOW to compare: look at the "salary" field of each dictionary
5. The lambda function `lambda x: x["salary"]` acts as the "measuring tape" – it extracts the salary from each dict
"""

employees = [
    {"name": "A", "salary": 20000},
    {"name": "B", "salary": 50000},
    {"name": "C", "salary": 30000},
]

def highest_salary(data):
    return max(data, key=lambda x: x["salary"])


if __name__=="__main":
    print(highest_salary(employees))