import json
import uuid

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
    print(f'Phone Number: {",".join(contact["phone_number"])}')
    print(f'Email: {contact["email"]}')
    print('-------------------------------')

def read_contact():
    print('\n----- All Contacts -----')
    print('ID\t\tFirst Name\tLast Name')
    for contact in contacts:
        print(f'{contact["id"]}\t{contact["first_name"]}\t\t{contact["last_name"]}')
    
    contact_id = input('\nEnter the ID of the contact you want to view: ')
    
    for contact in contacts:
        if contact['id'] == contact_id:
            display_contact(contact)
            break
    else:
        print('Contact not found.')

def update_contact():
    # update a contact
    # ask for the contact id
    # display the contact information
    # ask for the new contact information
    # update the contact in the contacts list
    # save the contacts to the file
    pass

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

# on exit, save the contacts to the file - or maybe save on every change?



# search and sort operations?