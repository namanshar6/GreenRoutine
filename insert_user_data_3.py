import mysql.connector
from getpass import getpass

# Function to connect to the MySQL database
def connect_to_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",   # Replace with your MySQL username
        password="shhreya123",  # Get the password securely
        database="greenroutine_db"
    )

# Function to insert data into 'users' table
def insert_user_data1(db_connection, username, email, password):
    cursor = db_connection.cursor()
    query = "INSERT INTO users (username, email, password) VALUES (%s, %s, %s)"
    cursor.execute(query, (username, email, password))
    db_connection.commit()  # Commit the transaction
    user_id = cursor.lastrowid  # Get the inserted user ID
    cursor.close()
    print(f"User '{username}' added with ID: {user_id}")
    return user_id

# Function to insert transportation habits
def insert_transportation_habits(db_connection, user_id):
    cursor = db_connection.cursor()

    transport_mode = input("Enter your primary mode of transport (e.g., car, bike, bus): ")
    weekly_usage_hours = input("Enter your weekly usage hours of the transport: ")
    daily_commute_distance = input("Enter your daily commute distance (in km): ")
    carpool = input("Do you carpool? (yes/no): ")
    interest_in_alternative_transport = input("Are you interested in alternative transport? (yes/no): ")

    # Insert into the 'transportation_habits' table
    query = """
        INSERT INTO transportation_habits 
        (user_id, transport_mode, weekly_usage_hours, daily_commute_distance, carpool, interest_in_alternative_transport)
        VALUES (%s, %s, %s, %s, %s, %s)
    """
    cursor.execute(query, (user_id, transport_mode, weekly_usage_hours, daily_commute_distance, carpool, interest_in_alternative_transport))

    # Commit the transaction
    db_connection.commit()
    print("Transportation habits added successfully.")

# Function to insert energy use habits
def insert_energy_use_habits(db_connection, user_id):
    cursor = db_connection.cursor()

    heating_cooling_method = input("Enter your heating/cooling method (e.g., AC, Heater): ")
    energy_conservation_habits = input("Describe your energy conservation habits: ")
    use_of_energy_efficient_appliances = input("Do you use energy-efficient appliances? (yes/no): ")
    interest_in_reducing_energy_consumption = input("Are you interested in reducing energy consumption? (yes/no): ")

    # Insert into the 'energy_use_habits' table
    query = """
        INSERT INTO energy_use_habits 
        (user_id, heating_cooling_method, energy_conservation_habits, use_of_energy_efficient_appliances, interest_in_reducing_energy_consumption)
        VALUES (%s, %s, %s, %s, %s)
    """
    cursor.execute(query, (user_id, heating_cooling_method, energy_conservation_habits, use_of_energy_efficient_appliances, interest_in_reducing_energy_consumption))

    # Commit the transaction
    db_connection.commit()
    print("Energy use habits added successfully.")

def main():
    # Connect to the database
    db_connection = connect_to_db()

    # Collect user data
    username = input("Enter your username: ")
    email = input("Enter your email: ")
    password = input("Enter your password: ")

    # Insert user data and get the user_id
    user_id = insert_user_data1(db_connection, username, email, password)
    enter_more_data = input("Do you want to enter transportation habits? (yes/no): ")
    if enter_more_data.lower() == 'yes':
        insert_transportation_habits(db_connection, user_id)

    enter_more_data = input("Do you want to enter energy use habits? (yes/no): ")
    if enter_more_data.lower() == 'yes':
        insert_energy_use_habits(db_connection, user_id)

    # Close the database connection
    db_connection.close()
    print("All data has been successfully inserted!")

# Entry point of the script
if __name__ == "__main__":
    main()
