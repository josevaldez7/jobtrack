applications = [{"Company" : "Google", 
                 "Position" : "Software Engineer", 
                 "Status" : "In Review"}]

def add_application (company, position, status):
    new_application = {"Company": company, 
                       "Position": position, 
                       "Status": status}
    applications.append(new_application)

def print_applications():
    for index, application in enumerate(applications): 
        print(f"Application #: {index + 1}")
        print(f"Company: {application['Company']}")
        print(f"Position: {application['Position']}")
        print(f"Status: {application['Status']}\n")
        
    print()

def update_application(application_number, new_information):
    applications[int(application_number) - 1]['Company'] = new_information[0]
    applications[int(application_number) - 1]['Position'] = new_information[1]
    applications[int(application_number) - 1]['Status'] = new_information[2]

def delete_application(application_number):
    applications.pop(application_number)

def get_valid_input(prompt, error_message):
    while True: 
        value = input(prompt).strip()

        if value: 
            return value
        
        print(error_message)


def main():
    while True:
        print("==========JOBTRACK==========")
        print("1. Add Application")
        print("2. View Applications")
        print("3. Update Application")
        print("4. Delete Application")
        print("5. Exit")
        user_input = input("Select an option: ")
        if not user_input.isdecimal():
            print("Enter valid menu option.\n")
            continue
        if int(user_input) == 5:
            break
        else: 
            match user_input:
                case "1":
                    company = get_valid_input("Enter company name: ", 
                                    "Company name cannot be empty. Try again. "
                            )

                    position = get_valid_input("Enter position title: ", 
                                               "Position name cannot be empty. Try again. "
                            )


                    status = get_valid_input("Enter application status: ", 
                                             "Status cannot be empty. Try again. "
                            )
                    add_application(company, position, status)
                    print()
                case "2":
                    print()
                    if not applications: 
                        print("Applications list is empty. Nothing to view.\n")
                        continue
                    print("Here are your current applications: ")
                    print_applications()
                case "3":
                    print()
                    print_applications()
                    
                    while True:
                        if not applications:
                            print("No applications to update. Add an application first. ")
                            break
                        application_number = input("Which Application would you like to update? (Enter application #) ")
                        if not application_number.isdecimal():
                            print("Enter a valid application number. ")
                            continue
                        if(0 < int(application_number) <= len(applications)):
                            company = get_valid_input("Enter company name: ", 
                                            "Company name cannot be empty. Try again. "
                                    )
                            position = get_valid_input("Enter position title: ", 
                                                    "Position name cannot be empty. Try again. "
                                    )
                            status = get_valid_input("Enter application status: ", 
                                                    "Status cannot be empty. Try again. "
                                    )
                            new_info = [company, position, status]
                            update_application(application_number, new_info)
                            break
                        else:
                            print("Enter a valid application number.")
                    print()
                    print_applications()
                case "4":
                    print_applications()

                    while True:
                        if len(applications) == 0:
                            print("No applications to delete.")
                            break
                                
                        application_number = input("Which application would you like to remove? (Enter application #) ")
                        if not application_number.isdecimal():
                            print("Enter a valid application number. ")
                            continue
                        if 0 < int(application_number) <= len(applications):
                            delete_application(int(application_number) - 1)
                            break
                        else: 
                           print("Enter a valid application number.")
                    print()
                    print_applications()
                case _:
                    print("Not a valid menu option. Try again.\n")

if __name__ == "__main__":
    main()
