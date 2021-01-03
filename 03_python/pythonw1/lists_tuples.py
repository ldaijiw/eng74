# collections in python

# Lists
# Lists are MUTABLE (i.e. changeable)

# shopping_list = ["apple", "banana", "milk", "bread"]
# print(shopping_list)
# # can verify it's a list with type()

# # indexing
# print(shopping_list[1])

# # adding an item at the end
# shopping_list.append("eggs")

# #removing an item
# shopping_list.remove("apple")
# print(shopping_list)

# # removing (last) item from list
# shopping_list.pop()
# print(shopping_list)

# # replacing an item in the list
# shopping_list[1] = "fruits"
# print(shopping_list)


# can have mixed data types in a list
mix_list = [10, 20, 30, "apple", 5.4, bool(True), "banana"]
print(mix_list)
print(type(mix_list))

# showing data types of each item
mix_list_types = {item: str(type(item)) for item in mix_list}
print(mix_list_types)


# # adding item
# mix_list.append(5)

# # remove item
# mix_list.remove("apple")

# # replace item
# mix_list[0] = "orange"

# # pop
# mix_list.pop(3)

# # print in reverse order
# print(mix_list)
# print(mix_list[::-1])


# Tuples are IMMUTABLE (i.e. can not be changed)
# Use cases NI number, DOB, place of birth etc.

my_tuple = ("paracetamol", "eggs", "supermalt")
print(type(my_tuple))


# item assignment will raise error
# my_tuple[1] = "fruits"