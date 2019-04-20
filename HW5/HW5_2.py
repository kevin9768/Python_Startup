#Library
#======================================================================================================
import json
import os

#variable
#======================================================================================================
operation = str
file_path = "account.json"

#Function
#======================================================================================================
def get_op():
    operation = str(input("create or search or exit: "))
    while operation != "create" and operation != "search" and operation != "exit":
        operation = str(input("create or search or exit: "))
    return operation

#Main function
#======================================================================================================
operation = get_op()
while operation != "exit":
    #check if json exists
    if os.path.isfile(file_path):
        with open(file_path, 'r') as file_object:
            contents = json.load(file_object)
    else:
        #create json file
        with open(file_path, 'w') as file_object:
            json.dump({}, file_object)
        contents = {}
    
    if operation == "search":
        ID = input("User ID(Enter exit to leave): ")
        while (ID in contents.keys()) == False and ID != 'exit':
            ID = str(input("ID not found, please retry or key in 'exit' to leave: "))
        if ID != 'exit':
            print("Password: %s" % contents[ID]['password'])
            ask = str(input("Would you like to revise the password? \nEnter 0 to revise 1 to exit: "))
            if ask == '0':
                newpw = str(input("Insert your new password: "))
                contents[ID]['password'] = newpw
                
    elif operation == "create":
        Name = str(input("User Name: "))
        ID = str(input("User ID: "))
        while ID in contents.keys():
            ID = str(input("ID is used, please retry another: "))
        PW = str(input("Password: "))
        keys = ["name", "password"]
        values = [Name, PW]
        unit = dict(zip(keys, values))
        contents[ID]=unit
    
    #update
    with open(file_path, 'w') as file_object:
        json.dump(contents, file_object)    
    
    #get new operation
    operation = get_op()