# Connects to DB and creates all of the tables
import pyodbc

class CreateTables:
    def __init__(self):
        server = "databases1.spartaglobal.academy"
        database = "Group_3_AirportDatabase"
        username = "SA"
        password = "Passw0rd2018"
        self.db_connection = pyodbc.connect(
            f'DRIVER=ODBC Driver 17 for SQL Server;SERVER={server};DATABASE={database};UID={username};PWD={password}')
        # create a class variable that's the cursor
        self.cursor = self.db_connection.cursor()

        self.cursor.execute("""               
        CREATE TABLE Passengers (
            Passenger_id INT IDENTITY(1,1) NOT NULL,
            PassportNumber VARCHAR(9) NOT NULL,
            FirstName VARCHAR(32) NOT NULL,
            LastName VARCHAR(32) NOT NULL,
            DateOfBirth DATE NOT NULL,
            PRIMARY KEY (Passenger_id) 
        );
        
        CREATE TABLE TicketDetails (
            Ticket_id INT IDENTITY(1,1) NOT NULL,
            Passenger_id INT NOT NULL,
            FlightTrip_id INT NOT NULL,
            PricePaid DECIMAL(6,2) NOT NULL,
            PRIMARY KEY (Ticket_id),
            FOREIGN KEY (Passenger_id) REFERENCES Passengers(Passenger_id),
            FOREIGN KEY (FlightTrip_id) REFERENCES FlightTrip(FlightTrip_id)
        );
        
        CREATE TABLE FlightTrip (
            FlightTrip_id INT IDENTITY(1,1) NOT NULL,
            AircraftAssigned VARCHAR(10) NOT NULL,
            DepartureTime DATETIME NOT NULL,
            ArrivalTime DATETIME NOT NULL,
            AvailableSeats INT NOT NULL,
            DepartureAirport VARCHAR(3) NOT NULL,
            ArrivalAirport VARCHAR(3) NOT NULL,
            TicketPrice DECIMAL(6,2) NOT NULL,
            TicketDiscount FLOAT NOT NULL,
            PRIMARY KEY (FlightTrip_id),
            FOREIGN KEY (AircraftAssigned) REFERENCES Aircraft(Aircraft_id),
            FOREIGN KEY (DepartureAirport) REFERENCES Airports(Airport_id),
            FOREIGN KEY (ArrivalAirport) REFERENCES Airports(Airport_id)
        );
        
        CREATE TABLE FlightStaff (
            FlightTrip_id INT NOT NULL,
            Staff_id INT NOT NULL,
            FOREIGN KEY (FlightTrip_id) REFERENCES FlightTrip(FlightTrip_id),
            FOREIGN KEY (Staff_id) REFERENCES Staff(Staff_id)
        );
        
        CREATE TABLE Staff (
            Staff_id INT IDENTITY(1,1) NOT NULL,
            Username VARCHAR(16) NOT NULL,
            FirstName VARCHAR(32) NOT NULL,
            LastName VARCHAR(40) NOT NULL,
            UserPassword VARCHAR(32) NOT NULL,
            PassportNumber VARCHAR(9) NOT NULL,
            PRIMARY KEY (Staff_id)
        );
        
        CREATE TABLE Aircraft (
            Aircraft_id INT IDENTITY(1,1) NOT NULL,
            AircraftType_id INT NOT NULL,
            FlightTrip_id INT NOT NULL,
            OnFlight INT NOT NULL,
            AssignedToFlight INT NOT NULL,
            CurrentAirport VARCHAR(3) NOT NULL,
            PRIMARY KEY (Aircraft_id),
            FOREIGN KEY (AircraftType_id) REFERENCES AircraftType(AircraftType_id),
            FOREIGN KEY (FlightTrip_id) REFERENCES FlightTrip(FlightTrip_id),
            FOREIGN KEY (CurrentAirport) REFERENCES Airports(Airport_id)
        );
        
        CREATE TABLE AircraftType (
            AircraftType_id INT IDENTITY(1,1) NOT NULL,
            Model VARCHAR(10) NOT NULL,
            MaxCapacity INT NOT NULL,
            PRIMARY KEY (AircraftType_id)
        );
        
        CREATE TABLE Airports (
            Airport_id VARCHAR(3) NOT NULL,
            AirportName VARCHAR(32) NOT NULL,
            AirportLocation VARCHAR(32) NOT NULL,
            Timezone INT NOT NULL,
            PRIMARY KEY (Airport_id)
        );
                        """)
