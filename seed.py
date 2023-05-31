import json
import uuid


#! I ran into an issue where I created the mock data before thinking about importing the UUID to generate random id values for each person
#! I moved the original mock data to temp.json.
#! Then I created a new file called seed.py to take the data from the temp.json file, add a UUID to each person (tested with a friends property first)
#! Then I added the new temp_data to the contacts.json file (for less issues, empty the contacts.json file first otherwise you will have duplicate data, maybe I'll figure that out later)

with open('temp.json', 'r') as temp_file: # this will open the temp.json file in read mode
    temp_data = json.load(temp_file) # this will load data from the temp.json file into the temp_data variable


for contact in temp_data:
    # contact['friends'] = 5  # This is a test to see if I can add a new key/value pair to each contact
    contact['id'] = str(uuid.uuid4()) # this will add an 'id' to each contact with a random UUID value


try:
    with open('contacts.json', 'r') as contacts_file: # this will open the contacts.json file in read mode
        contacts_data = json.load(contacts_file) # this will load data from the contacts.json file into the contacts_data variable (make empty unless you want to stack data on top of old data)
except json.decoder.JSONDecodeError:  # This is to catch the error if the contacts.json file is empty
    contacts_data = [] # This will create an empty list if the contacts.json file is empty

contacts_data += temp_data # This will add the temp_data to the contacts_data list


with open('contacts.json', 'w') as contacts_file: # this will open the contacts.json file in write mode
    json.dump(contacts_data, contacts_file, indent=4) # this will save the contacts to the file; indent=4 is optional for indenting and will make the file easier to read

print('Data has been merged and saved to contacts.json.')