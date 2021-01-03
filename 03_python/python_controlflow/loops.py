# for loops are used to iterate through data

shopping_list = ["eggs", "milk", "supermalt"]

for item in shopping_list:
    if item == "milk":
        print(item)


my_dict = {"name": "leo", "age": 21, "dob": "13071999"}


for key in my_dict.keys():
    print(key)

for value in my_dict.values():
    print(value)