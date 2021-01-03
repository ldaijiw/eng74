from nw_products import ProductManager

def main():
    new_pm = ProductManager()
    print(new_pm.table_information)
    print(new_pm.average_value("UnitsInStock"))
    print(new_pm.select_query("UnitPrice, UnitsInStock"))

if __name__ == "__main__":
    main()