import json

# Load available businesses from json file
with open('businesses.json', 'r') as f:
    businesses = json.load(f)

def add_business():
    new_business = {}
    new_business['name'] = input("Enter the name of the business: ")
    new_business['description'] = input("Enter a description of the business: ")
    new_business['address'] = input("Enter the address of the business: ")
    new_business['phone'] = input("Enter the phone number of the business: ")
    new_business['website'] = input("Enter the website of the business: ")
    print('Business added')
    
    # Generate a new unique ID for the business
    new_id = str(max([int(key) for key in businesses.keys()]) + 1)
    
    # Add the new business to the dictionary
    businesses[new_id] = new_business
    
    # Save businesses to json file
    with open('businesses.json', 'w') as f:
        json.dump(businesses, f)
        
def delete_business():
    name = input("Enter the name of the business you want to delete: ")
    for key, business in businesses.items():
        if business['name'] == name:
            del businesses[key]
            print(f"{name} has been deleted.")
            break
    else:
        print(f"{name} not found.")
    
def display_businesses():
    for key, business in businesses.items():
        print(f"ID: {key}")
        print(f"Name: {business['name']}")
        print(f"Description: {business['description']}")
        print(f"Address: {business['address']}")
        print(f"Phone: {business['phone']}")
        print(f"Website: {business['website']}")
        print()
        
while True:
    print("1. Add a business")
    print("2. Delete a business")
    print("3. Display all businesses")
    print("4. Quit")
    choice = input("Enter your choice: ")
    
    if choice == '1':
        add_business()
    elif choice == '2':
        delete_business()
    elif choice == '3':
        display_businesses()
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please try again.")
