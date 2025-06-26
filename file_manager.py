#File handling part

import csv

from contacts import Contact

file_name = "contact.csv"

contact_list = []

def new_contact():
    
    try:
        with open(file_name, mode= 'r', newline= "") as f:
            reader = csv.reader(f)
            for row in reader:
                if row: #to avoid empty lines
                    contact_info = Contact(*row)
                    contact_list.append(contact_info)
    except FileNotFoundError:
        open(file_name, 'w').close() #Create file if doesn't exist
    return contact_list
#this converts raw CSV data into objects that can be used in the OOP

def save_contact(contact_info): #to add a single new contact to the CSV file.
    with open(file_name, mode= 'a', newline= '') as f:
        writer = csv.writer(f)
        writer.writerow(contact_info.listing())

def save_contacts_2(contact_info): #for removing or updatring contacts
    with open(file_name, mode = 'w', newline= '') as f:
        writer = csv.writer(f)
        for contact_info in contact_list: 
            writer.writerow(contact_info.listing())

