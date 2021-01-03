import json


def openjson(filename):
    # open jsonfile in read format and return dictionary
    with open(filename, "r") as jsonfile:
        dict_from_json = json.load(jsonfile)
    return dict_from_json

def main():
    filename = "exchange_rates.json"
    # use openjson() to extract exchange_rates info from json file
    exchange_dict = openjson(filename)
    
    # contains 3 items: base currency, date, and exchange_rates (dict)
    base_currency = exchange_dict["base"]
    exchange_rates = exchange_dict["rates"]
    
    # iterate through each exchange rate and print
    for country, rate in exchange_rates.items():
        print(f"\nCOUNTRY: {country}, RATE: {rate}")



if __name__ == "__main__":
    main()