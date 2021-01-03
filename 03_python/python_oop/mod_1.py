# using __name__ and __main__

def main():
    # keyword pass allows to pass without an error
    pass

# checks whether code is run from current file
if __name__ == "__main__":

    print("This is mod_1 name ->", __name__)
    main()