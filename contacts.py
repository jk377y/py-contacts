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
def create_contact():
    # create a new contact
    # ask for the contact information
    # generate a unique id for the contact using uuid
    # add the contact to the contacts list
    # save the contacts to the file
    pass

def read_contact():
    # read a contact
    # ask for the contact id, or maybe a search option for the name?
    # display the contact information
    pass

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
While: True
print('\n-----Contacts Menu-----')
print('1. View a contact') # maybe add a search option here?
print('2. Add a contact')
print('3. Edit a contact') # display the contact and their information, then ask for the new info
print('4. Delete a contact')
print('5. Exit')




# on exit, save the contacts to the file - or maybe save on every change?



# search and sort operations?