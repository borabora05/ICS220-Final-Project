class Employee:  # Define a class named Employee

    def __init__(self, name, employeeID, department, jobTitle, basicSalary, age, dateOfBirth, passportDetails):
        # Constructor method to initialize the Employee object with provided attributes.

        self.name = name  # Assign the 'name' attribute with the provided name parameter.
        self.employeeID = employeeID  # Assign the 'employeeID' attribute with the provided employeeID parameter.
        self.department = department  # Assign the 'department' attribute with the provided department parameter.
        self.jobTitle = jobTitle  # Assign the 'jobTitle' attribute with the provided jobTitle parameter.
        self.basicSalary = basicSalary  # Assign the 'basicSalary' attribute with the provided basicSalary parameter.
        self.age = age  # Assign the 'age' attribute with the provided age parameter.
        self.dateOfBirth = dateOfBirth  # Assign the 'dateOfBirth' attribute with the provided dateOfBirth parameter.
        self.passportDetails = passportDetails  # Assign the 'passportDetails' attribute with the provided passportDetails parameter.

def display_employee_info():
    # Clear any existing entries and info labels on the GUI
    clear_entries()
    clear_info_label()
    # Define the fields for employee information entry
    employee_fields = ["Name:", "Employee ID:", "Department:", "Job Title:", "Basic Salary:", "Age:", "Date of Birth:", "Passport Details:"]
    # Iterate over the employee fields, creating corresponding labels and entry widgets
    for i, field in enumerate(employee_fields):
        tk.Label(info_frame, text=field).grid(row=i, column=0, sticky="e")  # Create a label for the field
        entry = tk.Entry(info_frame)  # Create an entry widget for user input
        entry.grid(row=i, column=1)  # Place the entry widget in the GUI grid
        employee_entries.append(entry)  # Add the entry widget to the list for later retrieval
