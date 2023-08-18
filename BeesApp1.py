import json
import mysql.connector

# Load businesses from JSON file
with open('businesses.json', 'r') as f:
    businesses = json.load(f)

# ... Other functions ...

def add_business():
    # Collect business details from user
    new_business = {}
    new_business['name'] = input("Enter the name of the business: ")
    new_business['description'] = input("Enter a description of the business: ")
    new_business['address'] = input("Enter the address of the business: ")
    new_business['phone'] = input("Enter the phone number of the business: ")
    new_business['website'] = input("Enter the website of the business: ")
    
    # ... Add other details ...
    
    # Add the new business to the dictionary
    new_id = str(max([int(key) for key in businesses.keys()]) + 1)
    businesses[new_id] = new_business
    
    # Save businesses to JSON file
    with open('businesses.json', 'w') as f:
        json.dump(businesses, f)
    
    # Insert data into MySQL database
    # ... Other code ...

try:
    connection = mysql.connector.connect(
        host="remote_host",
        user="root@localhost",
        password=" ",
        database="Business_information_hub"
    )
    cursor = connection.cursor()

    # ... Rest of the code ...

except mysql.connector.Error as error:
    print("Error: {}".format(error))
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()

# ... Rest of the code ...


        sql_insert_query = "INSERT INTO businesses (name, description, address, phone, website) VALUES (%s, %s, %s, %s, %s)"
        insert_data = (new_business['name'], new_business['description'], new_business['address'], new_business['phone'], new_business['website'])

        cursor.execute(sql_insert_query, insert_data)
        connection.commit()
        print("Business added and data inserted into MySQL database successfully!")

    except mysql.connector.Error as error:
        print("Error: {}".format(error))
    
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

while True:
