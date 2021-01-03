# Python JSON Task

- In this instance we will be using a JSON file with exchange rates and build your class around it.
- You will see from the exchange rates file that you will be accessing these data points as you would in a dictionary.
- Have exchange_rates.json file available 
- Display data from .json file
- iterate through data and display exchange rate by country

**SOLUTION NOTES**
- Information contained in **J**ava**S**cript **O**bject **N**otation format
 
```json
{
    "base": "EUR",
    "date": "2017-07-26",
    "rates": {
      "AUD": 1.4717,
      "BGN": 1.9558,
        .
        .
        .
      "ZAR": 15.2
    }
  }
```
- Has to be converted into a dictionary in Python so that it is accessible
```python
import json

def openjson(filename):
    # open jsonfile in read format and return dictionary
    with open(filename, "r") as jsonfile:
        dict_from_json = json.load(jsonfile)
    return dict_from_json
```

- To access ``exchange_rates.json``, must declare the correct filename to the ``openjson()`` function.
- Converting to dictionary ``exchange_dict = openjson(filename)``, reveals 3 keys: ``base``, ``date``, ``rates``
    - ``rates`` has a value of another dictionary, which contains all of the information regarding exchange rates for other countries.
    - After assigning that to a new variable ``exchange_rates = exchange_dict["rates"]`` can iterate through each item and print.
  
```python
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
```