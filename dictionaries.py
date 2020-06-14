student = {"name": "Jitendar",
    "age": 25,
    "courses": ["Math", "Comp Sc"]
}

print(student['courses'])
print(student.get("phone", "Not Found"))

student["phone"]= "555-55555"
print(student)

student.update({'name': 'Monalisa', 'age': 28, 'phone': '9606068624'})
print(student)

# del student["age"]
# print(student)

age1 = student.pop('age')
print(age1)
print(student)

print(student.items())

for key,value in student.items():
    print(key, value)