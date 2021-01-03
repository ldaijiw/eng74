# Have a look at practical use cases and implementation of try, except, raise, and finally

# create a var to store a file data using open()
# iter1
try:
    newfile = open("orders.txt")
except:
    print("Error loading file")


# iter2
try:
    file = open("orders.txt")
except FileNotFoundError as errmsg:
    print(f"Please create a file first\n{errmsg}")
    
    # will send back the actual exception
    raise errmsg
# finally executes regardless of above conditions
finally:
    print("Thank you")