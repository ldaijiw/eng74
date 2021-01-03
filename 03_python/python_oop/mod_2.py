import mod_1

# code being run in mod_2 file => name == main
print("This is mod_2 ->", __name__)
# since mod_1 is imported => name == mod_1
print("This is mod_1 ->", mod_1.__name__)