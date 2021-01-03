# use json module to do json encoding and decoding

import json

car_data = {"name": "tesla", "engine": "electric"}

print(car_data)


# json.dumps() - serialises json to a formatted string

car_data_json_string = json.dumps(car_data)
print(type(car_data_json_string))


# json.dump() creates a stream object and accept a file object to write to
# "w" gives write permissions
with open("new_json_file.json", "w") as jsonfile:
    json.dump(car_data, jsonfile)



# json.load() copies data and stores into variable
# "r" gives read permissions
with open("new_json_file.json", "r") as jsonfile:
    car = json.load(jsonfile)
    print(type(car))
    print(car["name"])


def read_json(filename):
    # attempts to execute this block first
    try:
        with open(filename, "r") as jsonfile:
            json_dict = json.load(jsonfile)
    
    # if type error occurs then runs this block
    except TypeError as e:
        print("Wrong type of file loaded")
        raise e
    
    # If no error occurs then executes this block
    else:
        print("File successfully read")
    
    # runs this block regardless of success or failure
    finally:
        print("Thank you for using read_json()")