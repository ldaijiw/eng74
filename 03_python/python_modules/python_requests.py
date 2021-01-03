import requests

live_response = requests.get("https://www.bbc.co.uk/")

print(live_response.status_code)

print(live_response.headers)
#print(live_response.content)

def check_response_code(live_response):
    if live_response.status_code == 200:
        print("Successful")
    elif live_response.status_code == 404:
        print("Site is unavailable at the moment, please try again later.")
    else:
        print("Something went wrong")


# second iteration


def bool_response_code(response):

    # will evaluate to True if status code is between 200-400, otherwise False
    if response.status_code == requests.codes.ok:
        print("Website is Live")
    elif response.status_code == requests.codes.not_found:
        print("Website is unavailable")
    else:
        print("Website is dead...")