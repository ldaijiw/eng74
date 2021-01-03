import pyodbc
import csv
from progress.bar import ChargingBar

class MovieDBManager:
    def __init__(self, user = 'daiji'):
        self.user = user
        self.start_connection()


    def start_connection(self, server = "databases1.spartaglobal.academy", database = "Northwind", username = "***", password = "***"):
        '''
        Starts connection to SQL DB with default credentials
        '''
        try:
            print("Establishing Connection")
            # connect to server with pyodbc.connect()
            self.db_connection = pyodbc.connect(f"DRIVER=ODBC Driver 17 for SQL Server;SERVER={server};DATABASE={database};UID={username};PWD={password}")
            # init cursor to execute queries
            self.cursor = self.db_connection.cursor()
        except:
            print("Something went wrong")
        
        else:
            # if no errors occurs prints following message
            print("Connection Successfully Made")
            self.database = database


    @classmethod
    def from_existing_table(cls, table_name):
        '''
        Class method to create instance from existing table name
        '''
        new_class = cls()
        new_class.table_name = table_name
        return new_class


    def create_table(self):
        '''
        Method to create table, prompts user to input path for data file and any changes to be made before creating table query
        '''

        create_from_data = True if input("\nCreate table from existing data?\n(y/n)\n") == "y" else False

        if create_from_data:
            file_read = False
            while not file_read:
                filename = input("\nPlease enter path for file\n")
                # attempt to extract data from given file path, if invalid will prompt again
                try:
                    # assigns class vars using data_from_file method
                    self.table_name, self.table_data = self.data_from_file(filename)
                    # assign column names from first row of data
                    self.column_names = self.table_data.pop(0)
                    self.column_names[0] = self.column_names[0][3:]

                except FileNotFoundError as errmsg:
                    print(errmsg)
                    print("\nSorry that's not a valid, path. Please try again.\n\n")

                else:
                    file_read = True
                    print("File successfully loaded\n")
                    print(f"TABLE NAME: {self.table_name}")
                    print(f"COLUMN NAMES: {self.column_names}")
                    print(f"{len(self.table_data)} ROWS TO BE ADDED")
        else:
            # option to create table from manually inserting data, to be added later
            return

        # Prompts user if they want to continue to table creation or alter any feature
        proceed = True if input("\nWould you like to proceed to table creation?\n(y/n)\n") == "y" else False

        while not proceed:
            # Asks user what they'd like to change
            attr_to_change = input("What would you like to change?\n(table name/column names)\n").lower().replace(' ', '_')

            if attr_to_change == 'table_name':
            # if table name entered then ask user for new table name
                self.table_name = input("\nPlease enter new table name\n")
                print(f"NEW TABLE NAME {self.table_name}")

            elif attr_to_change == 'column_names': 
                # if column names then ask which column they'd like to change
                column_to_change = int(input(f"\nWhich column would you like to change?\n0 - {len(self.column_names)-1}\n"))

                try:
                    # reassign column name from user input
                    self.column_names[column_to_change] = input("\nPlease enter new column name\n")

                except IndexError as errmsg:
                    print(errmsg)
                    print("Column index out of range, please try again")

                else:
                    print("Column name change successful\n")
                    print(f"NEW COLUMN NAMES\n{self.column_names}")

            else:
                print("Not recognised, please try again.")
                continue
            
            # if user doesn't want to make any other changes then proceed = True and loop breaks
            proceed = True if input("\nWould you like to make any other changes?\n(y/n)\n") == "n" else False
        
        print(f"TABLE NAME: {self.table_name}")
        print(f"COLUMN NAMES: {self.column_names}")
        print(f"{len(self.table_data)} ROWS TO BE ADDED")

        print("\n***\nCREATING TABLE\n***\n")

        # creates string containing the column information, formatted correctly to be added to the query
        column_info_str = ',\n'.join([f"{column_name} VARCHAR(255)" for column_name in self.column_names])

        # final string formatted correctly for SQL query
        create_table_query = f"CREATE TABLE {self.table_name}(\n{column_info_str});"
        
        try:
            # execute query
            self.cursor.execute(create_table_query)
        except:
            print("UNABLE TO CREATE TABLE")
            return
        else:
            print("\n***\nTABLE CREATED SUCCESSFULLY\n***\n")

        # progress bar to indicate progress of data insertion
        data_insertion_bar = ChargingBar('INSERTING DATA', max = len(self.table_data))
        # iterate through table data and insert data into table
        for data_row in self.table_data:
            self.insert_data(*data_row)
            data_insertion_bar.next()
            

        print("\n\n***\nDATA INSERTED SUCESSFULLY\n***\n")


    def insert_data(self, *data):
        '''
        Insert data into table, args passed are data values to be inserted
        '''
        # create string for data values, and column names, formatted correctly
        if not hasattr(self, 'table_name'):
            self.table_name = input("\nPlease enter table name to insert data into.\n")

        column_names = ', '.join(self.column_names)

        # if any values in data contain apostrophe, replace with double apostrophe to avoid formatting errors
        data = list(data)
        for i, item in enumerate(data):
            if "'" in item:
                data[i] = item.replace("'", "''")

        insert_data_str = ", ".join([f"'{item}'" for item in data])
        
        # final SQL query string formatted correctly
        insert_data_query = f"INSERT INTO {self.table_name}\n({column_names})\nVALUES({insert_data_str});"
        
        # execute insert_data_query
        self.cursor.execute(insert_data_query)


    def data_from_file(self, filepath, insert_data = False):
        '''
        Read data from filename passed as argument, if insert_data is True then will attempt to insert data into table directly, otherwise returns formatted data from file
        '''
        with open(filepath, "r") as datafile:
            # if file ends in csv then use csv.reader to open file
            if filepath[-3:] == "csv":
                table_data = list(csv.reader(datafile))
            
            # if file ends in txt then use read method and splitlines() to format data 
            elif filepath[-3:] == "txt":
                textdata_raw = datafile.read().replace(', ', ',').splitlines()
                table_data = [item.split(',') for item in textdata_raw]
            else:
                print("filepath not recognised")
                return
            
            if insert_data:
                print("INSERTING DATA FROM TEXT FILE")
                for item in table_data:
                    self.insert_data(*item)
            
            # table name assigned concatenating user name with filename, extracted from path
            table_name = f"{self.user}_{filepath[:-4].split('/')[-1]}"
            return table_name, table_data


    @property
    def table_information(self):
        '''
        Returns table info from SQL query
        '''
        table_info = self.cursor.execute(f'''
        SELECT
        TABLE_NAME,
        COLUMN_NAME
        FROM INFORMATION_SCHEMA.COLUMNS
        WHERE TABLE_NAME = '{self.table_name}';
        ''').fetchall()
        return table_info
        

    def select_query(self, select_details = "*"):
        '''
        Customisable SELECT query with default: SELECT *
        '''
        query = f"SELECT {select_details} FROM {self.table_name};"
        return self.cursor.execute(query).fetchall()[0]


    def find_movie(self, movie_title, select_details = "*"):
        '''
        Customisable SELECT query to find specific movie by title
        '''
        query = f"SELECT {select_details} FROM {self.table_name} WHERE primaryTitle IS {movie_title}"
        pass


    def delete_table(self, table_name):
        '''
        Method to drop table
        '''
        query = f"DROP TABLE {table_name};"
        self.cursor.execute(query)



def main():
    new_mdbm = MovieDBManager()
    new_mdbm.create_table()
    new_mdbm.data_from_file("movies_task/more_movies.txt", insert_data=True)

    print(new_mdbm.table_name)
    print(new_mdbm.table_information)
    print(new_mdbm.select_query())


if __name__ == "__main__":
    main()
    