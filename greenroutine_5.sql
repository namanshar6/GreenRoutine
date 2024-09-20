-- Create the database
CREATE DATABASE greenroutine_db;

-- Use the database
USE greenroutine_db;

-- Create 'users' table
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100),
    email VARCHAR(100),
    password VARCHAR(100)
);

-- Create 'transportation_habits' table
CREATE TABLE transportation_habits (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    transport_mode VARCHAR(50),
    weekly_usage_hours VARCHAR(50),
    daily_commute_distance VARCHAR(50),
    carpool VARCHAR(5),
    interest_in_alternative_transport VARCHAR(5),
    FOREIGN KEY (user_id) REFERENCES users(id)
);

-- Create 'energy_use_habits' table
CREATE TABLE energy_use_habits (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    heating_cooling_method VARCHAR(100),
    energy_conservation_habits VARCHAR(255),
    use_of_energy_efficient_appliances VARCHAR(50),
    interest_in_reducing_energy_consumption VARCHAR(5),
    FOREIGN KEY (user_id) REFERENCES users(id)
);

-- Create 'water_consumption_habits' table
CREATE TABLE water_consumption_habits (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    monitoring_water_usage_frequency VARCHAR(50),
    water_conservation_steps VARCHAR(5),
    FOREIGN KEY (user_id) REFERENCES users(id)
);

-- Create 'waste_recycling_habits' table
CREATE TABLE waste_recycling_habits (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    waste_management_method VARCHAR(100),
    recycling_frequency VARCHAR(50),
    use_of_waste_reduction_products VARCHAR(5),
    FOREIGN KEY (user_id) REFERENCES users(id)
);

-- Create 'food_diet_habits' table
CREATE TABLE food_diet_habits (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    prioritization_of_local_organic_produce VARCHAR(5),
    food_waste_frequency VARCHAR(50),
    interest_in_sustainable_eating VARCHAR(5),
    FOREIGN KEY (user_id) REFERENCES users(id)
);

-- Create 'shopping_consumption_habits' table
CREATE TABLE shopping_consumption_habits (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    shopping_frequency VARCHAR(50),
    consideration_of_environmental_impact VARCHAR(5),
    second_hand_sustainable_purchases_frequency VARCHAR(50),
    interest_in_reducing_consumption VARCHAR(5),
    FOREIGN KEY (user_id) REFERENCES users(id)
);

-- Create 'tech_smart_device_habits' table
CREATE TABLE tech_smart_device_habits (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    use_of_smart_devices VARCHAR(5),
    interaction_with_sustainability_apps VARCHAR(50),
    comfort_with_technology VARCHAR(5),
    FOREIGN KEY (user_id) REFERENCES users(id)
);
