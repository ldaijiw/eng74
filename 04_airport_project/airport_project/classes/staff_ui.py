# import pyodbc
# from time import sleep
# from os import system, name
# from datetime import datetime, timedelta
# from classes.booking_manager import BookingManager
# from classes.flight_trip_manager import FlightTripManager
# from classes.database_connector import DBConnector
# from classes.cryptic import Cryptic

# def clear():
#     if name == "nt":
#         _ = system('cls')
#     else:
#         _ = system("clear")


# # LEVEL 1 STAFF
# class StaffUI_1(DBConnector, BookingManager, FlightTripManager):
#     def __init__(self):
#         super().__init__()
#         self.user_options()
    
#     def user_options(self):
#         while True:
#             clear()
#             print("""
#             \n        WELCOME TO THE STAFF MENU - ACCESS LEVEL 1\n
#                 Options:
#                 0. Make a booking
#                 1. Create a new passenger
#                 2. Print a list of names of who's on a flight
#                 3. Logout

#                 TYPE <X> TO SHUTDOWN""")
#             choice = input("   ---> ").upper().strip()


#             if choice not in ["0", "1", "2", "3", "X"]:
#                 continue

            
#             # CHECKED
#             if choice == "X":
#                 clear()
#                 exit()


#             if choice == "0":
#                 self.staffui_make_booking()
#                 sleep(2)


#             if choice == "1":
#                 self.create_new_passenger()
#                 sleep(2)

#             if choice == "2":
#                 self.print_list_flight_names()
#                 sleep(2)

#             if choice == "3":
#                 clear()
#                 return "RETURNED LOGOUT"


#     # OPTION 0
#     def staffui_make_booking(self):
#         y = self.cursor.execute("SELECT FlightTrip_id FROM FlightTrip;")
#         list_of_flights_check = []
#         for row in y:
#             list_of_flights_check.append(row[0])

#         print("\nCurrent Flight ID's:", list_of_flights_check, "\n")

#         for f_id in list_of_flights_check:
#             x = self.cursor.execute(f"SELECT DepartureAirport, ArrivalAirport FROM FlightTrip WHERE FlightTrip_id = {f_id}").fetchone()
#             x = list(x)
#             print(f"{f_id} : {x[0]} to {x[1]}")

#         while True:
#             flight_to_add = input("\nInput FlightTrip ID or X to go back: ").strip().upper()

#             if flight_to_add == "X":
#                 return print("\nMaking booking aborted")

#             if not flight_to_add.isdigit():
#                 print("\nWrong input format, try again")
#                 continue

#             if int(flight_to_add) not in list_of_flights_check:
#                 print("\nNo such flight!")
#                 continue
#             else:
#                 flight_to_add = int(flight_to_add)
#                 break

#         while True:       
#             id_input = input("Please input the passenger_id's, separated by commas: ")
#             list_to_add = id_input.split(",")
#             for val in list_to_add:
#                 if not val.isdigit():
#                     continue
#             break

#         list_to_add = list(map(lambda x: x.strip(), list_to_add))
#         list_to_add = list(map(lambda x: int(x), list_to_add))
        
#         self.make_booking(flight_to_add, list_to_add)
#         print("\nPassengers added")
#         input("\nPress <ENTER> to continue")


#     # OPTION 1
#     # CHECKED
#     def create_new_passenger(self):
#         # INPUT: FIRST NAME, LAST NAME, DOB, GENDER, PASSPORT NUMBER
#         firstname = input("\nInput first name: ").title().strip()
#         lastname = input("Input last name: ").title().strip()

#         while  True:
#             dob = input("Enter date of birth (YYYY-MM-DD): ").strip()
#             check_list = dob.split("-")
#             for val in check_list:
#                 if not val.isdigit():
#                     continue
#             break

#         gender = input("Input gender: ").title().strip()
#         while True:
#             passportnumber = input("Input a 9-digit Passport number: ").strip()
#             if len(passportnumber) != 9:
#                 print("\nPlease input the exact 9-digit Passport number")
#                 continue
#             elif not passportnumber.isdigit():
#                 print("\nOnly digits please")
#                 continue
#             else:
#                 break

#         print("\nThanks!")
#         # Checks for duplicate username entries and disallows them
#         y = self.cursor.execute("SELECT PassengerUsername FROM PassengerLogins;")
#         list_of_usernames_check = []
#         for row in y:
#             list_of_usernames_check.append(row[0])

#         while True:
#             user_name = input("Choose a username: ").strip()
#             if user_name in list_of_usernames_check:
#                 print("\nUsername taken!")
#                 continue
#             else:
#                 break
#         pass_word = input("Choose a password: ").strip()

#         print(self.create_passenger(firstname, lastname, dob, gender, passportnumber,user_name, pass_word))
#         input("\nPress <ENTER> to continue")


#     # OPTION 2
#     # CHECKED
#     def print_list_flight_names(self):
#         y = self.cursor.execute("SELECT FlightTrip_id FROM FlightTrip;")
#         list_of_flights_check = []
#         for row in y:
#             list_of_flights_check.append(row[0])

#         print("\nCurrent Flight ID's:", list_of_flights_check)

#         while True:
#             flight_trip_id = input("Enter FlightTrip ID: ").strip()
#             if not flight_trip_id.isdigit():
#                 print("\nPlease input valid numbers")
#                 continue
#             if int(flight_trip_id) not in list_of_flights_check:
#                 print("\nNo such choice, pick again")
#                 continue
#             else:
#                 flight_trip_id = int(flight_trip_id)
#                 break
        
#         tup = self.flight_attendees_list(flight_trip_id)
#         self.print_flight_attendees_list(tup)
#         input("\nPress <ENTER> to continue")



# # LEVEL 2 STAFF
# class StaffUI_2(DBConnector, BookingManager, FlightTripManager):
#     def __init__(self):
#         super().__init__()
#         self.user_options()


#     # This shows the available options for the user
#     def user_options(self):
#         while True:
#             clear()
#             print("""

#             \n        WELCOME TO THE STAFF MENU - ACCESS LEVEL 2\n
#                 Options:
#                 0. Make a booking
#                 1. Create a new staff member
#                 2. Create a new passenger
#                 3. Create a new flight trip
#                 4. Assign an aircraft to an existing flight trip
#                 5. Change the aircraft being used for a flight trip
#                 6. Check staff availability
#                 7. Assign staff to a flight
#                 8. Calculate the income from a flight
#                 9. Print a list of names of who's on a flight
#                 10. LOGOUT

#                 TYPE <X> TO SHUTDOWN""")
#             choice = input("  ---> ").upper().strip()


#             if choice not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "X"]:
#                 continue

            
#             # CHECKED
#             if choice == "X":
#                 clear()
#                 exit()


#             if choice == "0":
#                 self.staffui_make_booking()
#                 sleep(1)


#             if choice == "1":
#                 self.create_new_staff_member()
#                 sleep(1)


#             if choice == "2":
#                 self.create_new_passenger()
#                 sleep(1)


#             if choice == "3":
#                 self.create_new_flight_trip()
#                 sleep(1)


#             if choice == "4":
#                 self.assign_aircraft_to_existing_flight_trip()
#                 sleep(1)


#             if choice == "5":
#                 self.change_aircraft_in_trip()
#                 input("\nPress <ENTER> to continue")
#                 sleep(1)


#             if choice == "6":
#                 self.check_flight_staff_available()
#                 sleep(1)


#             if choice == "7":
#                 self.assign_staff_to_existing_flight()
#                 sleep(1)


#             if choice == "8":
#                 self.calculate_income_from_flight()
#                 sleep(1)


#             if choice == "9":
#                 self.print_list_flight_names()
#                 sleep(1)

#             if choice == "10":
#                 clear()
#                 return "RETURNED LOGOUT"

#     # OPTION 0
#     def staffui_make_booking(self):
#         y = self.cursor.execute("SELECT FlightTrip_id FROM FlightTrip;")
#         list_of_flights_check = []
#         for row in y:
#             list_of_flights_check.append(row[0])

#         print("\nCurrent Flight ID's:", list_of_flights_check, "\n")

#         for f_id in list_of_flights_check:
#             x = self.cursor.execute(f"SELECT DepartureAirport, ArrivalAirport FROM FlightTrip WHERE FlightTrip_id = {f_id}").fetchone()
#             x = list(x)
#             print(f"{f_id} : {x[0]} to {x[1]}")

#         while True:
#             flight_to_add = input("\nInput FlightTrip ID or X to go back: ").strip().upper()

#             if flight_to_add == "X":
#                 return print("\nMaking booking aborted")

#             if not flight_to_add.isdigit():
#                 print("\nWrong input format, try again")
#                 continue

#             if int(flight_to_add) not in list_of_flights_check:
#                 print("\nNo such flight!")
#                 continue
#             else:
#                 flight_to_add = int(flight_to_add)
#                 break

#         while True:       
#             id_input = input("Please input the passenger_id's, separated by commas: ")
#             list_to_add = id_input.split(",")
#             for val in list_to_add:
#                 if not val.isdigit():
#                     continue
#             break

#         list_to_add = list(map(lambda x: x.strip(), list_to_add))
#         list_to_add = list(map(lambda x: int(x), list_to_add))
        
#         self.make_booking(flight_to_add, list_to_add)
#         print("\nPassengers added")
#         input("\nPress <ENTER> to continue")
    
#     # OPTION 1
#     # CHECKED
#     def create_new_staff_member(self):
#         # INPUT: JOB_ID, FIRST NAME, LAST NAME, USERNAME, PASSWORD, PASSPORT NUMBER, GENDER, ON LOCATION, STAFF LEVEL
#         while True:
#             print("\nJOB ID:\n1 = Airport Staff\n2 = Flight Crew")
#             job = input("\nWhat's their job? ").strip()
#             if job not in ["1", "2"]:
#                 print("\nNot a valid option, choose again")
#                 continue
#             job = int(job)
#             break

#         firstname = input("Input first name: ").title().strip()
#         lastname = input("Input last name: ").title().strip()
        
#         # Check if username is there already and doesn't allow duplicates
#         y = self.cursor.execute("SELECT StaffUsername FROM StaffLogins;")
#         list_of_usernames_check = []
#         for row in y:
#             list_of_usernames_check.append(row[0])

#         while True:
#             username = input("Choose a username: ").strip()
#             if username in list_of_usernames_check:
#                 print("\nUsername taken!")
#                 continue
#             else:
#                 break

#         password = input("Create a password: ").strip()
#         while True:
#             passportnumber = input("Input the 9-digit Passport number: ").strip()
#             if len(passportnumber) != 9:
#                 print("\nPlease input the exact 9-digit number")
#                 continue
#             elif not passportnumber.isdigit():
#                 print("\nInput only digits")
#                 continue
#             else:
#                 break
            
#         gender = input("Input gender: ").title()
#         on_location = 1

#         while True:
#             staff_level = input("\nWhat level of access do they have? ").strip()
#             if staff_level not in ["1", "2"]:
#                 print("Invalid option, choose either level 1 or level 2")
#                 continue
#             else:
#                 break

#         print(self.create_staff(job, firstname, lastname, username, password, passportnumber, gender, on_location, staff_level))
#         input("\nPress <ENTER> to continue")

#     # OPTION 2
#     # CHECKED
#     def create_new_passenger(self):
#         # INPUT: FIRST NAME, LAST NAME, DOB, GENDER, PASSPORT NUMBER
#         firstname = input("\nInput first name: ").title().strip()
#         lastname = input("Input last name: ").title().strip()

#         while  True:
#             dob = input("Enter date of birth (YYYY-MM-DD): ").strip()
#             check_list = dob.split("-")
#             for val in check_list:
#                 if not val.isdigit():
#                     continue
#             break

#         gender = input("Input gender: ").title().strip()
#         while True:
#             passportnumber = input("Input a 9-digit Passport number: ").strip()
#             if len(passportnumber) != 9:
#                 print("\nPlease input the exact 9-digit Passport number")
#                 continue
#             elif not passportnumber.isdigit():
#                 print("\nOnly digits please")
#                 continue
#             else:
#                 break

#         print("\nThanks!")
#         # Checks for duplicate username entries and disallows them
#         y = self.cursor.execute("SELECT PassengerUsername FROM PassengerLogins;")
#         list_of_usernames_check = []
#         for row in y:
#             list_of_usernames_check.append(row[0])

#         while True:
#             user_name = input("Choose a username: ").strip()
#             if user_name in list_of_usernames_check:
#                 print("\nUsername taken!")
#                 continue
#             else:
#                 break
#         pass_word = input("Choose a password: ").strip()

#         print(self.create_passenger(firstname, lastname, dob, gender, passportnumber,user_name, pass_word))
#         input("\nPress <ENTER> to continue")
    
#     # OPTION 3
#     # CHECKED
#     def create_new_flight_trip(self):
#         try:
#             departuredate = input("\nChoose a departure date (YYYY-MM-DD): ").strip()
#             departuretime = input("Choose departure time (HH:MM): ").strip()
#             date_in_list = departuredate.split("-")
#             time_in_list = departuretime.split(":")
#             year, month, day, hour, minute = int(date_in_list[0]), int(date_in_list[1]), int(date_in_list[2]), int(time_in_list[0]), int(time_in_list[1])
#             dt_input = datetime(year, month, day, hour, minute)
#         except:
#             print("\nTry again!")
#             return self.create_new_flight_trip()

#         y = self.cursor.execute("SELECT Airport_id From Airports")
#         airport_list_check = []
#         for row in y:
#             airport_list_check.append(row[0])
        
#         print("\nKnown airports:", airport_list_check)
#         while True:
#             arrivalairport = input("Choose an airport to arrive at: ").upper().strip()
#             if arrivalairport not in airport_list_check:
#                 print("No flight routes there!")
#                 continue

#             if arrivalairport == "LHR":
#                 print("Invalid option! Choose any other airport apart from LHR")
#                 continue
#             else:
#                 break

#         while True:
#             ticketprice = input("\nHow much are tickets? ")
#             ticketdiscount = input("What's the discount? ")
#             if ticketprice.isdigit() and ticketdiscount.isdigit():
#                 ticketprice = int(ticketprice)
#                 ticketdiscount = int(ticketdiscount)
#                 break
#             else:
#                 print("Input valid values!")
#                 continue


#         self.create_flight_trip(dt_input, arrivalairport, ticketprice, ticketdiscount)
#         print("\nAdded!")
#         while True:
#             choose = input("\nWould you like to assign an aircraft to this flight (Y/N)? ").strip().upper()
#             if choose in ["Y", "YES", "1"]:
#                 self.assign_aircraft_to_existing_flight_trip()
#             else:
#                 break
#         input("Press <ENTER> to continue")
        
        
#     # OPTION 4
#     # CHECKED
#     def assign_aircraft_to_existing_flight_trip(self):
#         y = self.cursor.execute("SELECT FlightTrip_id FROM FlightTrip WHERE Aircraft_id IS NULL;")
#         list_of_flights_check = []
#         for row in y:
#             list_of_flights_check.append(row[0])

#         if not list_of_flights_check:
#             print("\nAll flights have assigned aircrafts")
#             return input("\nPress <ENTER> to continue")

#         print("\nCurrent Flight ID's that require an aircraft:", list_of_flights_check)
#         for f_id in list_of_flights_check:
#             x = self.cursor.execute(f"SELECT DepartureAirport, ArrivalAirport FROM FlightTrip WHERE FlightTrip_id = {f_id}").fetchone()
#             x = list(x)
#             print(f"{f_id} : {x[0]} to {x[1]}")

#         while True:
#             flight_to_add = input("\nInput FlightTrip ID or X to go back: ").strip().upper()
#             if flight_to_add == "X":
#                 return print("\nAdding aircraft aborted")

#             if not flight_to_add.isdigit():
#                 print("\nWrong input format, try again")
#                 continue

#             if int(flight_to_add) not in list_of_flights_check:
#                 print("\nNo such flight!")
#                 continue
#             else:
#                 break
        
#         self.assign_aircraft(flight_to_add)
#         print(f"\nThe next available aircraft was assigned to flight {flight_to_add}")
        

#     # OPTION 5
#     # CHECKED
#     def change_aircraft_in_trip(self):
#         y = self.cursor.execute("SELECT FlightTrip_id FROM FlightTrip;")
#         list_of_flights_check = []
#         for row in y:
#             list_of_flights_check.append(row[0])

#         print("\nCurrent Flight ID's:", list_of_flights_check)
#         for f_id in list_of_flights_check:
#             x = self.cursor.execute(f"SELECT DepartureAirport, ArrivalAirport FROM FlightTrip WHERE FlightTrip_id = {f_id}").fetchone()
#             x = list(x)
#             print(f"{f_id} : {x[0]} to {x[1]}")

#         while True:
#             flight_to_add = input("\nInput FlightTrip ID (X to cancel): ").strip().upper()

#             if flight_to_add == "X":
#                 return print("\nAdding aircraft cancelled")

#             if not flight_to_add.isdigit():
#                 print("\nWrong input format, try again")
#                 continue

#             if int(flight_to_add) not in list_of_flights_check:
#                 print("\nNo such flight!")
#                 continue
#             else:
#                 break
        
#         self.change_aircraft(flight_to_add)
#         print("\nAircraft changed")
#         input("\nPress <ENTER> to continue")

#     # OPTION 6
#     # FINALISED
#     def check_flight_staff_available(self):
#         list_of_staff = self.check_staff_availability()
#         print("\nCurrent flight crew available:")
#         print("\nStaff_id  FirstName  LastName")
#         for row in list_of_staff:
#             print(f"{row[0]}  {row[1]}  {row[2]}")

#         retr = []
#         for staff_id in list_of_staff:
#             retr.append(staff_id[0])
#         return retr

#     # OPTION 7
#     # CHECKED
#     def assign_staff_to_existing_flight(self):
#         y = self.cursor.execute("SELECT FlightTrip_id FROM FlightTrip;")
#         list_of_flights_check = []
#         for row in y:
#             list_of_flights_check.append(row[0])

#         print("\nCurrent Flight ID's:", list_of_flights_check)
#         for f_id in list_of_flights_check:
#             x = self.cursor.execute(f"SELECT DepartureAirport, ArrivalAirport FROM FlightTrip WHERE FlightTrip_id = {f_id}").fetchone()
#             x = list(x)
#             print(f"{f_id} : {x[0]} to {x[1]}")

#         while True:
#             flight_to_add = input("\nInput FlightTrip ID (Type X to exit): ").strip().upper()
#             if flight_to_add == "X":
#                 break

#             if not flight_to_add.isdigit():
#                 print("\nWrong input format, try again")
#                 continue

#             if int(flight_to_add) not in list_of_flights_check:
#                 print("No such flight!")
#                 continue
#             else:
#                 break
            
#         list_of_ids_check = self.check_flight_staff_available()
#         print(list_of_ids_check)
        
#         while True:       
#             id_input = input("\nPlease input the Staff ID's to add from the list, separated by commas:\n")
#             try:
#                 list_to_add = id_input.split(",")
#             except:
#                 print("\nTry again")
#                 continue
#             error_list = []
#             for val in list_to_add:
#                 if not val.isdigit():
#                     print("\nWrong format, try again")
#                     continue
#                 if int(val) not in list_of_ids_check:
#                     error_list.append(val)
#                     print(error_list)
#             if error_list:
#                 print("\nThe following staff aren't available:", error_list)
#                 continue        
#             break

#         list_to_add = list(map(lambda x: x.strip(), list_to_add))
#         list_to_add = list(map(lambda x: int(x), list_to_add))

#         try:
#             self.assign_staff_to_flight(flight_to_add, list_to_add)
#             print("\nAdded!")
#             input("\nPress <ENTER> to continue")
#         except:
#             print("\nTry again!")


#     # OPTION 8
#     # CHECKED
#     def calculate_income_from_flight(self):
#         y = self.cursor.execute("SELECT FlightTrip_id FROM FlightTrip;")
#         list_of_flights_check = []
#         for row in y:
#             list_of_flights_check.append(row[0])

#         print("\nCurrent Flight ID's:", list_of_flights_check)
#         for f_id in list_of_flights_check:
#             x = self.cursor.execute(f"SELECT DepartureAirport, ArrivalAirport FROM FlightTrip WHERE FlightTrip_id = {f_id}").fetchone()
#             x = list(x)
#             print(f"{f_id} : {x[0]} to {x[1]}")
        
#         while True:
#             id_to_sum = input("Check income from which flight? ").strip()
#             if not id_to_sum.isdigit():
#                 print("\nPlease input valid numbers")
#                 continue
#             if int(id_to_sum) not in list_of_flights_check:
#                 print("\nNo such choice, pick again")
#                 continue
#             else:
#                 id_to_sum = int(id_to_sum)
#                 break

#         print("")
#         print(self.calculate_ticket_income(id_to_sum))
#         input("\nPress <ENTER> to continue")

        
#     # OPTION 9
#     # CHECKED
#     def print_list_flight_names(self):
#         y = self.cursor.execute("SELECT FlightTrip_id FROM FlightTrip;")
#         list_of_flights_check = []
#         for row in y:
#             list_of_flights_check.append(row[0])

#         print("\nCurrent Flight ID's:", list_of_flights_check)
#         for f_id in list_of_flights_check:
#             x = self.cursor.execute(f"SELECT DepartureAirport, ArrivalAirport FROM FlightTrip WHERE FlightTrip_id = {f_id}").fetchone()
#             x = list(x)
#             print(f"{f_id} : {x[0]} to {x[1]}")

#         while True:
#             flight_trip_id = input("\nEnter FlightTrip ID: ").strip()
#             if not flight_trip_id.isdigit():
#                 print("\nPlease input valid numbers")
#                 continue
#             if int(flight_trip_id) not in list_of_flights_check:
#                 print("\nNo such choice, pick again")
#                 continue
#             else:
#                 flight_trip_id = int(flight_trip_id)
#                 break
        
#         tup = self.flight_attendees_list(flight_trip_id)
#         self.print_flight_attendees_list(tup)
#         input("\nPress <ENTER> to continue")



# if __name__ == "__main__":
#     f = StaffUI_2()
