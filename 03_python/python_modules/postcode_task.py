import requests

# research how to convert this data into dictionary
# hint - python json library
# iterate through data and print results

# iterate through data and print results
# print longitude and latitude


def postcode_response():
    user_postcode = str(input("Please enter your postcode\n").strip().lower())

    url = "http://api.postcodes.io/postcodes/"
    url_target = url + user_postcode
    live_response = requests.get(url_target)
    return live_response

def get_coordinates(response):
    # .json() converts to json format which is dictionary of 2 keys (status, result)
    # result dictionary contains all information in dictionary format
    response_results = response.json()["result"]

    return (response_results["longitude"], response_results["latitude"])


def check_response_code(response):
    return response.json()["status"]


def display_response_results(response):
    return response.json()["result"]


def main():
    user_response = postcode_response()
    print(check_response_code(user_response))
    print(display_response_results(user_response))
    print(get_coordinates(user_response))


if __name__ == "__main__":
    main()