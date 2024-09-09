# Name: Eli Thomas
# Date: 9/4/2024
# File Purpose: 

contact_list_ = []

def print_list(list_):
	print("\n========= CONTACT LIST ==========")
	print("Index    First Name   Last Name")
	index = 0
	for contact in contact_list_:
		print("{:<8} {:<12} {:<12}".format(index, contact['first'], contact['last']))
		index += 1
"""
def add_contact(first, last):
	contact = {'first': first, 'last': last}
	contact_list_.append(contact)
	return contact_list_
"""
def add_contact(fullname):
	contact_list_.append(fullname)
	return contact_list_

def modify_contact(index, modified_contact):
	if(index > len(contact_list_)):
		print("Invalid index number.")
		return contact_list_
	contact_list_[index] = modified_contact
	return contact_list_
	
def delete_contact(index, fullname):
	if(index > len(contact_list_)):
		print("Invalid index number.")
		return contact_list_
	contact_list_.pop(index)
	return contact_list_
	
def print_menu():
	print("\n     *** TUFFY TITAN CONTACT MAIN MENU ***     ")
	print("1. Print list")
	print("2. Add contact")
	print("3. Modify contact")
	print("4. Delete contact")
	print("5. Exit program\n")
	return
