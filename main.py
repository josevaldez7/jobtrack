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

def main_menu():

    while True:
        print("==========JOBTRACK==========")
        print("1. Add Application")
        print("2. View Applications")
        print("3. Update Application")
        print("4. Delete Application")
        print("5. Exit")
        user_input = input("Select an option: ")
        if int(user_input) == 5:
            break
        else: 
            match user_input:
                case "1":
                    company = input("Enter company name: ")
                    position = input("Enter position title: ")
                    status = input("Enter application status: ")
                    add_application(company, position, status)
                case "2":
                    print_applications()

main_menu()
