import json # this will import the json module
import uuid # this will import the uuid module
from tabulate import tabulate # this will import the tabulate module for displaying the contacts in a table


with open('contacts.json', 'r') as file:
    contacts = json.load(file) # this will load the contacts from the file into the contacts variable

with open('contacts.json', 'w') as file:
    json.dump(contacts, file) # this will save the contacts to the file


def create_contact(): # this is the create operation for the new_contact; it accepts the information from the user and creates a new contact
    first_name = input('Enter the first name: ')
    last_name = input('Enter the last name: ')
    birthdate = input('Enter the birthdate: ')
    phone_number = input('Enter the phone number: ')
    email = input('Enter the email address: ')
    
    new_contact = { # this is a dictionary data structure that will hold the new_contact information
        'id': str(uuid.uuid4()),
        'first_name': first_name,
        'last_name': last_name,
        'birthdate': birthdate,
        'phone_number': phone_number,
        'email': email
    }
    contacts.append(new_contact) # this will add the new_contact to the contacts.json file

    with open('contacts.json', 'w') as file: # this will open the contacts.json file in write mode
        json.dump(contacts, file) # this will save the contacts to the file

    print('Contact added successfully!')
    

def display_contact(contact): # this is the display operation for the contact; it accepts the contact information and displays it to the user
    print('\n----- Contact Information -----')
    print(f'ID: {contact["id"]}')
    print(f'First Name: {contact["first_name"]}')
    print(f'Last Name: {contact["last_name"]}')
    print(f'Birthdate: {contact["birthdate"]}')
    print(f'Phone Number: {contact["phone_number"]}')
    print(f'Email: {contact["email"]}')
    print('-------------------------------')

def read_contact(): # this is the read operation for the contact; it accepts the contact information and displays it to the user
    table = [] # this is an empty list that will hold the contacts
    for contact in contacts:
        table.append([contact["id"], contact["first_name"], contact["last_name"]]) # this will append the chosen data to the table list

    headers = ['ID', 'First Name', 'Last Name'] # this is a list that will hold the headers for the table
    print(tabulate(table, headers, tablefmt='grid')) # this will print the table to the console using the headers defined, and the tablefmt='grid' will make the table look better, then populating the table with the data from the table list
    
    contact_id = input('\nEnter the ID of the contact you want to view: ') # this will prompt the user to enter the ID of the contact they want to view
    
    for contact in contacts:
        if contact['id'] == contact_id: # this will check if the contact_id matches any contact['id'] in the contacts.json file
            display_contact(contact) # if that contact_id exists, this will display the contact information to the user
            break
    else:
        print('Contact not found.')

def update_contact(): # this is the update operation for the contact; it accepts the contact information and updates it to the user
    table = [] # this is an empty list that will hold the contacts
    for contact in contacts: 
        table.append([contact["id"], contact["first_name"], contact["last_name"]]) # this will append the chosen data to the table list

    headers = ['ID', 'First Name', 'Last Name'] # this is a list that will hold the headers for the table
    print(tabulate(table, headers, tablefmt='grid')) # this will print the table to the console using the headers defined, and the tablefmt='grid' will make the table look better, then populating the table with the data from the table list

    contact_id = input('\nEnter the ID of the contact you want to update: ') # this will prompt the user to enter the ID of the contact they want to update

    for contact in contacts:
        if contact['id'] == contact_id: # this will check if the contact_id matches any contact['id'] in the contacts.json file
            display_contact(contact) # if that contact_id exists, this will display the contact information to the user
            
            # instead of requiring the user to enter all the fields, we will ask them which fields they want to update
            # and only update those fields
            print('\nSelect the fields you want to update:')
            print('1. First Name')
            print('2. Last Name')
            print('3. Birthdate')
            print('4. Phone Number')
            print('5. Email')
            print('6. Done\n')

            fields_to_update = [] # this is an empty list that will hold the fields to update
            done = False # this is a boolean variable that will be used to check if the user is done updating the contact; it is set to False by default and will be set to True when the user selects '6. Done' (see code for while Not done:)

            while not done:
                choice = input('Enter your choice: ')

                if choice == '1':
                    fields_to_update.append('first_name')
                elif choice == '2':
                    fields_to_update.append('last_name')
                elif choice == '3':
                    fields_to_update.append('birthdate')
                elif choice == '4':
                    fields_to_update.append('phone_number')
                elif choice == '5':
                    fields_to_update.append('email')
                elif choice == '6':
                    done = True
                else:
                    print('Invalid choice!')

            for field in fields_to_update: # this will loop through the fields_to_update list 
                value = input(f'Enter the new value for {field}: ') # and ask the user to enter the new value for each field
                contact[field] = value # this will update the contact[field] with the new value
                print(f'{field} updated successfully!') # this will print a message to the user that the field was updated successfully

            # Save the updated contacts to the file
            with open('contacts.json', 'w') as file:
                json.dump(contacts, file, indent=4) # json.dump will save the contacts to the file, and indent=4 will make the file look better

            print('Contact updated successfully!')
            break
    else:
        print('Contact not found.')

def delete_contact(): # this is the delete operation for the contact; it accepts the contact_id from the user and deletes it upon confirmation
    table = [] # this is an empty list that will hold the contacts
    for contact in contacts:
        table.append([contact["id"], contact["first_name"], contact["last_name"]]) # this will append the chosen data to the table list

    headers = ['ID', 'First Name', 'Last Name'] # this is a list that will hold the headers for the table
    print(tabulate(table, headers, tablefmt='grid')) # this will print the table to the console using the headers defined, and the tablefmt='grid' will make the table look better, then populating the table with the data from the table list

    contact_id = input('\nEnter the ID of the contact you want to delete: ') # this will prompt the user to enter the ID of the contact they want to delete

    for contact in contacts: # this will loop through the contacts.json file
        if contact['id'] == contact_id: # this will check if the contact_id matches any contact['id'] in the contacts.json file
            print('\nConfirm deletion:')
            print(f'Delete {contact["first_name"]} {contact["last_name"]}') # this will ask the user to confirm the deletion of the contact
            confirm = input('Enter "yes" to confirm or any other key to cancel: ') # this will prompt the user to enter 'yes' to confirm or any other key to cancel

            if confirm.lower() == 'yes':
                contacts.remove(contact) # this will remove the contact from the contacts.json file if the user confirms the deletion
                with open('contacts.json', 'w') as file:
                    json.dump(contacts, file, indent=4)
                print(f'{contact["first_name"]} {contact["last_name"]} deleted successfully!') # this will print a message to the user that the contact was deleted successfully
            else:
                print('Deletion canceled.')
            break
    else:
        print('Contact not found.')

# need to define a menu system for the user to interact with the contacts
while True:
    print('\n-----Contacts Menu-----')
    print('1. View a contact') # maybe add a search option here?
    print('2. Add a contact')
    print('3. Edit a contact') # display the contact and their information, then ask for the new info
    print('4. Delete a contact')
    print('5. Exit')

    choice = input('\nEnter your choice: ')

    if choice == '1':
        read_contact()
    elif choice == '2':
        create_contact()
    elif choice == '3':
        update_contact()
    elif choice == '4':
        delete_contact()
    elif choice == '5':
        break # this will exit the loop and end the program
    else:
        print('Invalid choice!')
        continue # this will go back to the top of the loop and display the menu again if the user enters an invalid choice
