# Name: Eli Thomas
# Date: 9/4/2024
# File Purpose: main driver for contact menu

from contacts import *

exit_program = False
contact_list = []

while exit_program == False:

	print_menu()
	
	print("Enter menu choice: ")
	choice = int(input())
	
	if choice == 1:
		print_list(contact_list)
	if choice == 2:
		first = input("Enter first name: ")
		last = input("Enter last name: ")
		add_contact(contact_list, first, last)
	if choice == 3:
		modify_contact()
	if choice == 4:
		delete_contact()
	if choice == 5:
		exit_program = True

