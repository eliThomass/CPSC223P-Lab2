# Name: Eli Thomas
# Date: 9/4/2024
# File Purpose: 

def print_list(list_):
	for name in list_:
		print(name)

def add_contact(list_,first, last):
	list_.append([first,last])
"""
def modify_contact(first, last):
	return

def delete_contact(first, last):
	return
"""
def print_menu():
	print("")
	print("     *** TUFFY TITAN CONTACT MAIN MENU ***     ")
	print("1. Print list")
	print("2. Add contact")
	print("3. Modify contact")
	print("4. Delete contact")
	print("5. Exit program")
	print("")
	return
