# A List of numbers
marks = [85, 90, 78, 92, 88]
print(marks)
print(type(marks))

# A list of strings
fruits = ["apple", "banana", "cherry"]
print(fruits)
print(type(fruits))
print(fruits[0])
print(fruits[1])
print(fruits[2])
# print(fruits[3]) # out of index error

# Negative index = from the end:
print(fruits[-1])
print(fruits[-2])
print(fruits[-3])

# A mix (usually we avoid mixing, but it works)
mixed = ["Aayush", 24, True]
print(mixed)
print(type(mixed))

# update an item by assigning a new value
marks = [85, 90, 78, 92]
marks[2] = 80
print(marks)

fruits = ["apple", "banana"]
fruits.append("cherry")
print(fruits)

fruits.insert(1, "orange")
print(fruits)

# Dictionary

student = {
    "name": "Aayush",
    "age": 24,
    "gender": "Male"
}
print(student)  
print(type(student))

# print(student["name"])
# print(student["age"])
# print(student["gender"])

print(student.get("name"))
print(student.get("age"))
print(student.get("gender"))
print(student.get("degree"))

student["degree"] = "B.Tech"
print(student["degree"])
print(student)

student = {
    "name": "Dhruvi",
    "age": 24,
    "course": "MSc IT",
    "cgpa": 9.9
}

for key in student.keys():
    print("Key: ", key)

for value in student.values():
    print("Value: ", value)

for key, value in student.items():
    print(key, "=>", value)

student = {
    "name": "Dhruvi",
    "roll_no": 101,
    "subjects": ["Python", "Math", "AI"],   # note: a list inside dict
    "is_active": True
}

# set

numbers = {1, 2, 3, 4}
print(numbers)
print(type(numbers))

fruits_list = ["apple", "banana", "apple", "mango"]
fruits_set = set(fruits_list)
print(fruits_set)
print(type(fruits_set))

fruits = {"apple", "banana"}
print(fruits)
print(type(fruits))

fruits.add("mango")
print(fruits)  # {"apple", "banana", "mango"}

fruits.discard("banana")
print(fruits)  # {"apple", "mango"}

cs_students = {"Amit", "Bhavya", "Dhruvi"}
math_students = {"Bhavya", "Chirag", "Dhruvi"}

both = cs_students & math_students
print(both)

either = cs_students | math_students
print(either)

cs_only = cs_students - math_students
print(cs_only)

math_only = math_students - cs_students
print(math_only)