# Write a Python script that reads "data.json" representing employee information.
# Implement a function that calculates and returns the average salary of all employees.
# Create a new JSON entry for a new employee with your own information (name, role, gender, date of birth, phone, and salary).
# Add the new employee entry to the existing JSON data.
# Save the modified JSON data to a new file.
import json


with open('data.json', 'r', encoding='utf8') as file:
    data = json.load(file)

#print(data['employees'])

# salary = 0
# employeecount = 0
#
# for employee in data['employees']:
#     salary += employee['salary']
#     employeecount += 1
#     avg = salary/employeecount
# print(avg)
def average_salary():
    total_salaries = 0
    for person in data['employees']:
        total_salaries += person['salary']
    return total_salaries/len(data['employees'])

new_json = '''{
    "name": "Somebody Surname",
    "role": "Product Owner",
    "gender": "female",
    "info": {
        "date_of_birth": "11.11.2011",
        "phone": "111111111"
        },
    "salary": 2500
}'''

updated_data_dict = json.loads(new_json)
data['employees'].append(updated_data_dict)
# print(data)
updated_data = json.dumps(data, indent=2)
print(updated_data)

with open('new.json', 'w', encoding='utf8') as file:
    file.write(updated_data)

print(average_salary())