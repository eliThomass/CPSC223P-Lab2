# Name: Eli Thomas
# Date: 9/4/2024
# File Purpose: Main driver for contact menu

from contacts import *

exit_program = False

while exit_program == False:

	print_menu()

	choice = int(input("Enter menu choice: "))
	
	if choice == 1:
		print_list()
		
	elif choice == 2:
		first = input("Enter first name: ")
		last = input("Enter last name: ")
		contact = [first, last]
		add_contact(contact)
		
	elif choice == 3:
		if len(contact_list_) == 0:
			print("List is empty!")
			continue
		modify_contact(contact_list_)
		
	elif choice == 4:
		index = int(input("Enter index to modify: "))
		delete_contact(index)
		
	elif choice == 5:
		exit_program = True

