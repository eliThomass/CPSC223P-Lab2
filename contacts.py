# Name: Eli Thomas
# Date: 9/4/2024
# File Purpose: 

def print_list(list_):
	print("==========CONTACT LIST===========")
	
	for name in list_:
		print(name)

def add_contact(list_,first, last):
	list_.append([first,last])
	return list_

def modify_contact(list_, index, first, last):
	if(index > len(list_)):
		print("Invalid index number.")
		return list_
	list_[index] = [first, last]
	return list_
	
def delete_contact(list_, index,):
	if(index > len(list_)):
		print("Invalid index number.")
		return list_
	list_.pop(index)
	return list_
	
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
