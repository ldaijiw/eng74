import pyodbc
import getpass
from os import system, name
from time import sleep
from classes.database_connector import DBConnector
from classes.passenger_ui import Passenger
#from classes.staff_ui import StaffUI_1, StaffUI_2
import pandas
from tabulate import tabulate
from classes.cryptic import Cryptic


def clear():
    if name == "nt":
        _ = system('cls')
    else:
        _ = system("clear")

class LogIn(DBConnector):
    # def __init__(self):
    #     super().__init__()
    #     while True:
    #         print("  ______________________________________________ ")
    #         print(" | Please enter:                                |")
    #         print(" |                1. Passenger                  |")
    #         print(" |                2. Staff                      |")
    #         print(" |                                              |")
    #         answer = input(" |       ==> ")
    #         print(" |______________________________________________|")

    #         if answer[0] in ["1", "p", "P"]:
    #             Passenger()
    #             break
    #         elif answer[0] in ["2", "s", "S"]:
    #             self.log_in()
    #             break
    #         else:
    #             print("not an option")


    # def log_in(self, username, input_password):
    #     i = 0
    #     self.staff = True
    #     crypto = Cryptic() # Create object of class
    #     while True:
    #         clear()
    #         i += 1
    #         # if i > 5:
    #             # IF LOG IN FAILED 5 TIMES SHUT THEM OUT
    #         #     print("\nYou have been shut out of the system!")
    #         #     input("\nPress <ENTER> to exit")
    #         #     exit()


    #         # print("  ______________________________________________ ")
    #         # print(" |  Login Page                                  |")
    #         # print(" |                                              |")
    #         # username = input(" |        Username: ").strip()
    #         # print(" |                                              |")
    #         # input_password = getpass.getpass(" |        Password: ")
    #         # print(" |______________________________________________|")


    #         # LOAD IN THE RELEVANT PASSENGERS AND STAFF LOG IN DETAILS
    #         if self.staff:
    #             # IF STAFF ALSO LOAD IN THERE RANK
    #             login_details = self.cursor.execute(f"SELECT StaffUsername, StaffPassword, StaffLevel FROM StaffLogins WHERE StaffUsername = '{username}';").fetchone()
    #             if login_details == None:
    #                 #print("\nUsername not recognised!\n")
    #                 #input("\nPress <ENTER> to continue")
    #                 return LogIn()

    #             login_details = list(login_details)
    #             print(login_details)
    #             database_username = login_details[0]
    #             database_password = crypto.decrypt(login_details[1])
    #             database_stafflevel = login_details[2]

    #         else:
    #             login_details = self.cursor.execute(f"SELECT PassengerUsername, PassengerPassword FROM PassengerLogins WHERE PassengerUsername = '{username}';").fetchone()
    #             if login_details == None:
    #                 #print("\nUsername not recognised!\n")
    #                 #input("\nPress <ENTER> to continue")
    #                 return LogIn()
    #             login_details = list(login_details)
    #             login_details.append(0)
    #             database_username = login_details[0]
    #             database_password = crypto.decrypt(login_details[1])
    #             database_stafflevel = login_details[2]


    #         if input_password != database_password:
    #             #print("\nPassword Incorrect\n")
    #             #input("\nPress <ENTER> to continue")
    #             continue
    #         else:
    #             # clear()
    #             # print("  ______________________________________________ ")
    #             # print(" |  Login Page                                  |")
    #             # print(" |                                              |")
    #             # print(" |           LOGIN SUCCESSFUL!                  |")
    #             # print(" |               LOADING.                       |")
    #             # print(" |                                              |")
    #             # print(" |______________________________________________|")
    #             # sleep(0.7)
    #             # clear()
    #             # print("  ______________________________________________ ")
    #             # print(" |  Login Page                                  |")
    #             # print(" |                                              |")
    #             # print(" |           LOGIN SUCCESSFUL!                  |")
    #             # print(" |               LOADING..                      |")
    #             # print(" |                                              |")
    #             # print(" |______________________________________________|")
    #             # sleep(0.7)
    #             # clear()
    #             # print("  ______________________________________________ ")
    #             # print(" |  Login Page                                  |")
    #             # print(" |                                              |")
    #             # print(" |           LOGIN SUCCESSFUL!                  |")
    #             # print(" |               LOADING...                     |")
    #             # print(" |                                              |")
    #             # print(" |______________________________________________|")
    #             # sleep(0.7)


    #             if self.staff:
    #                 if database_stafflevel == 1:
    #                     # RUN STAFF 1 CAPABILITIES
    #                     # retr = StaffUI_1()

    #                     #if retr == "RETURNED LOGOUT":
    #                     #    return LogIn()

    #                     return login_details[0], login_details[1]

    #                 if database_stafflevel == 2:
    #                     # RUN STAFF 2 CAPABILITIES
    #                     # retr = StaffUI_2()

    #                     #if retr == "RETURNED LOGOUT":
    #                     #    return LogIn()

    #                     return login_details[0], login_details[1]


    #             if self.passenger:
    #                 # RUN PASSENGER CAPABILITIES
    #                 Passenger()
    #                 return login_details[0], login_details[1], login_details[2]

    def log_in(self, username, password):
        i = 0
        while True:
            i += 1
            # print("  ______________________________________________ ")
            # print(" | Staff Login Page                             |")
            # print(" |                                              |")
            # username = input(" |        Username: ")
            # print(" |                                              |")
            # password = input(" |        Password: ")
            # print(" |______________________________________________|")
            
            login_details = self.cursor.execute(f"SELECT Username, UserPassword FROM Staff WHERE Username = '{username}';").fetchone()
            if len(login_details) == 0:
                print("\nUsername not recognised!\n")
            elif password != list(login_details)[1]:
                print("\nPassword Incorrect\n")
            elif i > 5:
                print(" You have been shut out of the system! ")
                break
            elif [username, password] == list(login_details):
                # print("  ______________________________________________ ")
                # print(" | Staff Login Page                             |")
                # print(" |                                              |")
                # print(" |          LOGIN SUCCESSFUL!                   |")
                # print(" |                                              |")
                # print(" |______________________________________________|")
                return username, password
if __name__ == '__main__':
    login = LogIn()