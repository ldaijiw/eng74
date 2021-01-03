# dictionary
# another way of managing data more dynamically
# uses items in the form of key: value pairs to store and manage data

devops_student_data = {
    "key": "value",
    "name": "james",
    "stream": "tech",
    "completed_lessons": 4,
    "completed_lesson_names": ["operators", "data types", "variables"]
}

# verifying it's a dictionary
print(type(devops_student_data))

print(devops_student_data["name"])
print(devops_student_data["completed_lesson_names"][1])


# finding keys
devops_student_data.keys()

# finding values
devops_student_data.values()

# finding items
devops_student_data.items()


# removing item from list in dictionary
devops_student_data["completed_lesson_names"].remove("operators")

# appending item to list in dictionary
devops_student_data["completed_lesson_names"].append("collections")