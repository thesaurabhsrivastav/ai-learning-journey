student = {
    "name": "Rahul",
    "age": 21
}

print(student["name"])

#Add New Data
student["city"] = "Delhi"
student["age"] = 22


for key in student:
    print(key)

for value in student.values():
    print(value)

for key, value in student.items():
    print(key, value)

student.pop("age")
student.clear()

students = {
    "student1": {
        "name": "Rahul",
        "marks": 90
    },

    "student2": {
        "name": "Aman",
        "marks": 85
    }
}

student.get("name") #This will retrun NONE if not exists
student["phone"] #This may crash if not exists

text = "apple banana apple mango banana apple"

words = text.split()

count = {}

for word in words:

    if word in count:
        count[word] += 1

    else:
        count[word] = 1

print(count)