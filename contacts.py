import json
import uuid
from tabulate import tabulate

# need to define a data structure for the contacts, like a model in MVC
# id, first name, last name, birthdate, phone number, email address

# on startup, load the contacts from the file

with open('contacts.json', 'r') as file:
    contacts = json.load(file) # this will load the contacts from the file into the contacts variable

with open('contacts.json', 'w') as file:
    json.dump(contacts, file) # this will save the contacts to the file

# need to utilize CRUD operations on the contacts
# create_contact is working as intended - will probably remove the seed files once everything is fully functional
def create_contact(): # this is the create operation for the new_contact; it accepts the information from the user and creates a new contact
    first_name = input('Enter the first name: ')
    last_name = input('Enter the last name: ')
    birthdate = input('Enter the birthdate: ')
    phone_number = input('Enter the phone number: ')
    email = input('Enter the email address: ')
    
    new_contact = { # this is a dictionary that will hold the new contact information
        'id': str(uuid.uuid4()),
        'first_name': first_name,
        'last_name': last_name,
        'birthdate': birthdate,
        'phone_number': phone_number,
        'email': email
    }
    contacts.append(new_contact) # this will add the new contact to the contacts.json file

    with open('contacts.json', 'w') as file:
        json.dump(contacts, file)

    print('Contact added successfully!')
    

def display_contact(contact):
    print('\n----- Contact Information -----')
    print(f'ID: {contact["id"]}')
    print(f'First Name: {contact["first_name"]}')
    print(f'Last Name: {contact["last_name"]}')
    print(f'Birthdate: {contact["birthdate"]}')
    print(f'Phone Number: {contact["phone_number"]}')  # Updated key to "phone_number"
    print(f'Email: {contact["email"]}')
    print('-------------------------------')

def read_contact():
    table = []
    for contact in contacts:
        table.append([contact["id"], contact["first_name"], contact["last_name"]])

    headers = ['ID', 'First Name', 'Last Name']
    print(tabulate(table, headers, tablefmt='grid'))
    
    contact_id = input('\nEnter the ID of the contact you want to view: ')
    
    for contact in contacts:
        if contact['id'] == contact_id:
            display_contact(contact)
            break
    else:
        print('Contact not found.')

def update_contact():
    table = []
    for contact in contacts:
        table.append([contact["id"], contact["first_name"], contact["last_name"]])

    headers = ['ID', 'First Name', 'Last Name']
    print(tabulate(table, headers, tablefmt='grid'))

    contact_id = input('\nEnter the ID of the contact you want to update: ')

    for contact in contacts:
        if contact['id'] == contact_id:
            display_contact(contact)
            print('\nSelect the fields you want to update:')
            print('1. First Name')
            print('2. Last Name')
            print('3. Birthdate')
            print('4. Phone Number')
            print('5. Email')
            print('6. Done')

            fields_to_update = []
            done = False

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

            for field in fields_to_update:
                value = input(f'Enter the new value for {field}: ')
                contact[field] = value
                print(f'{field} updated successfully!')

            # Save the updated contacts to the file
            with open('contacts.json', 'w') as file:
                json.dump(contacts, file, indent=4)

            print('Contact updated successfully!')
            break
    else:
        print('Contact not found.')

def delete_contact():
    # delete a contact
    # ask for the contact id
    # remove the contact from the contacts list
    # save the contacts to the file
    pass

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
