# Name: Eli Thomas
# Date: 9/4/2024
# File Purpose: main driver for contact menu

from contacts import *

exit_program = False
contact_count = 0

while exit_program == False:

	print_menu()

	choice = int(input("Enter menu choice: "))
	
	if choice == 1:
		print_list()
		
	elif choice == 2:
		first = input("Enter first name: ")
		last = input("Enter last name: ")
		contact = {'first': first, 'last': last}
		add_contact(contact)
		
	elif choice == 3:
		if len(contact_list_) == 0:
			print("List is empty!")
			continue
		index = int(input("Enter index to modify: "))
		first = input("Enter first name: ")
		last = input("Enter last name: ")
		contact = {'first': first, 'last': last}
		modify_contact(index, contact)
		
	elif choice == 4:
		index = int(input("Enter index to modify: "))
		delete_contact(index)
		
	elif choice == 5:
		exit_program = True

