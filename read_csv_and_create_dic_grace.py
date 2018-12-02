


def read_csv_and_create_dic(fileobj):

	student_id_data = {}

	file = fileobj.readlines()
	remove_first_line = file[1:]

	for line in remove_first_line:
		line = line.strip()
		word = line.split(",")
		student_names = word[0]
		student_id = word[1]
		final_score = word[2]
		final_grade = word[3]
		student_id_data[student_id] = {}
		student_id_data[student_id]["Student Name"] = student_names
		student_id_data[student_id]["Final Score"] = final_score
		student_id_data[student_id]["Final Grade"] = final_grade

	return student_id_data


def create_new_student_data_file():
	pass


def update_an_existing_student_data_file():
	pass


def remove_a_student():
	pass


def search_a_student():
	pass


def print_only_summary_of_student_data():
	pass



def print_the_entire_student_data_from_command_line():
	pass



def student_data_manager():


	while True:
		print("1 - Create new student data file.")
		print("2 - Update an existing student data file")
		print("3 - Remove a student")
		print("4 - Search a student")
		print("5 - Print only summary of student data")
		print("6 - Print the entire student data from command line")

		option = int(input("Please choose one of the menu options: 1,2,3,4,5,6, or 0 to quit\n"))

		if option == 0:
			print("You've selected the option to quit bye bye")
			break
		elif option == 1:
			create_new_student_data_file()
		elif option == 2:
			update_an_existing_student_data_file()
		elif option == 3:
			remove_a_student()
		elif option == 4:
			search_a_student()
		elif option == 5:
			print_only_summary_of_student_data()
		elif option == 6:
			print_the_entire_student_data_from_command_line()
		else:
			print("Please select an option 0-6")


def main():

	with open("existing_student_data.csv", "r") as fileobj:
		print(read_csv_and_create_dic(fileobj))


	student_data_manager()




main()