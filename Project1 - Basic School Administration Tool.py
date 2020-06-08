import csv


def write_into_file(info_list):
    with open('student_info.csv', 'a', newline='') as csvfile:
        info_writer = csv.writer(csvfile)
        if csvfile.tell() == 0:
            info_writer.writerow(["NAME", "AGE", "MOBILE NO.", "EMAIL ID"])
        info_writer.writerow(student_info_list)


if __name__ == '__main__':
    condition = True
    stud_num = 1
    while condition:
        student_info = input("\nEnter information of student #{} in the following format - Name,Age,Mobile No.,"
                             "Email ID: ".format(stud_num))
        student_info_list = student_info.split(",")
        print("\nEntered Information: \nNAME: {} \nAGE: {} \nMOBILE NO.: {} \nEMAIL ID: {}".format(student_info_list[0], student_info_list[1], student_info_list[2], student_info_list[3]))

        entered_val1 = True
        while entered_val1:
            check = input("\nIs the entered information correct? type (yes/no): ")

            if check == "yes":
                write_into_file(student_info_list)

                entered_val2 = True
                while entered_val2:
                    choice = input("\nDo you want to enter another student's information? type (yes/no): ")
                    if choice == "no":
                        condition = False
                        entered_val2 = False
                    elif choice == "yes":
                        condition = True
                        stud_num += 1
                        entered_val2 = False
                    else:
                        print("Invalid Input. Please re-enter")
                entered_val1 = False

            elif check == "no":
                print("\nPlease re-enter the information")
                entered_val1 = False

            else:
                print("Invalid Input. Please re-enter")
