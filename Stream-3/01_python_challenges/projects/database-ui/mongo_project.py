# Import credentials from mongo_connection.py
from mongo_connection import MONGODB_URI, DBS_NAME, COLLECTION_NAME, mongo_connect

        
# Interface for interacting with database
def show_menu():
    print("")
    print("1. Add a Record to the Database.")
    print("2. Read Data from the Database.")
    print("3. Update Data from the Database.")
    print("4. Delete a Record.")
    print("5. Exit.")
    print("")
    option = input("Enter an option >>> ")
    return option
    

# Helper function
def get_record():
    print("")
    first = input("Enter first name >>> ")
    last = input("Enter last name >>> ")
    
    try:
        doc = coll.find_one({"first": first.capitalize(), "last": last.capitalize()})
    except:
        print("Error accessing the database.Please try again.")
    
    if not doc:
        print("")
        print("Error! No results found.")
    
    return doc


## CRUD Functions ##

# Create 
def add_record():
    first = input("Enter first name. >>> ")
    last = input("Enter last name. >>> ")
    dob = input("Enter date of birth. >>> ")
    occupation = input("Enter occupation. >>> ")
    nationality = input("Enter nationality. >>> ")
    
    new_doc = {"first": first.title(), "last": last.title(), "dob": dob.lower(), "occupation": occupation.lower(), "nationality": nationality.lower()}
    
    try:
        coll.insert(new_doc)
        print("")
        print("Document added to database.")
    except:
        print("Error. Could not add record.")
    

# Read
def find_record():
    doc = get_record()
    if doc:
        print("")
        for k, v in doc.items():
            if k != "_id":
                print(k.title() + ": " + v.title())
    

# Update 
def update_record():
    doc = get_record()
    if doc:
        update_doc = {}
        print("")
        for k, v in doc.items():
            if k != "_id":
                update_doc[k] = input(k.capitalize() + " [" + v + "] > ")
                
                if update_doc[k] == "":
                    update_doc[k] = v
        
        try:       
            coll.update_one(doc, {"$set": update_doc})
            print("")
            print("Document updated.")
        except:
            print("Error accessing the database. Please try again.")
        

# Delete
def delete_record():
    doc = get_record()
    if doc:
        print("")
        for k, v in doc.items():
            if k != "_id":
                print(k.title() + ": " + v.title())
        
        print("")
        confirmation = input("Is this the document you want to delete?\nY or N > ")
        print("")
        
        if confirmation.lower() == "y":
            try:
                coll.remove(doc)
                print("Document deleted.")
            except:
                print("Error accessing the database. Please try again.")
        else:
            print("Operation not completed.")
            print("Document not deleted.")


def main_loop():
    while True:
        option = show_menu()
        if option == "1":
            print("Option 1.")
            print("")
            add_record()
        elif option == "2":
            print("Option 2.")
            print("")
            find_record()
        elif option == "3":
            print("Option 3.")
            print("")
            update_record()
        elif option == "4":
            print("Option 4.")
            print("")
            delete_record()
        elif option == "5":
            print("Bye.")
            conn.close()
            break
        else:
            print("Invalid option. Please try again.")


# The database and collection to be queried for this program
conn = mongo_connect(MONGODB_URI)
coll = conn[DBS_NAME][COLLECTION_NAME]


# Run
main_loop()
