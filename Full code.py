import tkinter as tk
from tkinter import ttk, messagebox
import pickle
import os

# Define classes based on the UML diagram
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


class Client:  # Define a class named Client

    def __init__(self, clientID, name, address, contactDetails, budget):
        # Constructor method to initialize the Client object with provided attributes.

        self.clientID = clientID  # Assign the 'clientID' attribute with the provided clientID parameter.
        self.name = name  # Assign the 'name' attribute with the provided name parameter.
        self.address = address  # Assign the 'address' attribute with the provided address parameter.
        self.contactDetails = contactDetails  # Assign the 'contactDetails' attribute with the provided contactDetails parameter.
        self.budget = budget  # Assign the 'budget' attribute with the provided budget parameter.


class Event:  # Define a class named Event

    def __init__(self, eventID, type, theme, date, time, duration, venue, client, guests, cateringCompany, cleaningCompany, decorationsCompany, entertainmentCompany, furnitureSupplier, invoice):
        # Constructor method to initialize the Event object with provided attributes.

        self.eventID = eventID  # Assign the 'eventID' attribute with the provided eventID parameter.
        self.type = type  # Assign the 'type' attribute with the provided type parameter.
        self.theme = theme  # Assign the 'theme' attribute with the provided theme parameter.
        self.date = date  # Assign the 'date' attribute with the provided date parameter.
        self.time = time  # Assign the 'time' attribute with the provided time parameter.
        self.duration = duration  # Assign the 'duration' attribute with the provided duration parameter.
        self.venue = venue  # Assign the 'venue' attribute with the provided venue parameter.
        self.client = client  # Assign the 'client' attribute with the provided client parameter.
        self.guests = guests  # Assign the 'guests' attribute with the provided guests parameter.
        self.cateringCompany = cateringCompany  # Assign the 'cateringCompany' attribute with the provided cateringCompany parameter.
        self.cleaningCompany = cleaningCompany  # Assign the 'cleaningCompany' attribute with the provided cleaningCompany parameter.
        self.decorationsCompany = decorationsCompany  # Assign the 'decorationsCompany' attribute with the provided decorationsCompany parameter.
        self.entertainmentCompany = entertainmentCompany  # Assign the 'entertainmentCompany' attribute with the provided entertainmentCompany parameter.
        self.furnitureSupplier = furnitureSupplier  # Assign the 'furnitureSupplier' attribute with the provided furnitureSupplier parameter.
        self.invoice = invoice  # Assign the 'invoice' attribute with the provided invoice parameter.


class Guest:  # Define a class named Guest

    def __init__(self, guestID, name, address, contactDetails):
        # Constructor method to initialize the Guest object with provided attributes.

        self.guestID = guestID  # Assign the 'guestID' attribute with the provided guestID parameter.
        self.name = name  # Assign the 'name' attribute with the provided name parameter.
        self.address = address  # Assign the 'address' attribute with the provided address parameter.
        self.contactDetails = contactDetails  # Assign the 'contactDetails' attribute with the provided contactDetails parameter.

class Venue:  # Define a class named Venue

    def __init__(self, venueID, name, address, contact, minGuests, maxGuests):
        # Constructor method to initialize the Venue object with provided attributes.

        self.venueID = venueID  # Assign the 'venueID' attribute with the provided venueID parameter.
        self.name = name  # Assign the 'name' attribute with the provided name parameter.
        self.address = address  # Assign the 'address' attribute with the provided address parameter.
        self.contact = contact  # Assign the 'contact' attribute with the provided contact parameter.
        self.minGuests = minGuests  # Assign the 'minGuests' attribute with the provided minGuests parameter.
        self.maxGuests = maxGuests  # Assign the 'maxGuests' attribute with the provided maxGuests parameter.

class Caterer:  # Define a class named Caterer

    def __init__(self, catererID, name, address, contactDetails, menu, minGuests, maxGuests):
        # Constructor method to initialize the Caterer object with provided attributes.

        self.catererID = catererID  # Assign the 'catererID' attribute with the provided catererID parameter.
        self.name = name  # Assign the 'name' attribute with the provided name parameter.
        self.address = address  # Assign the 'address' attribute with the provided address parameter.
        self.contactDetails = contactDetails  # Assign the 'contactDetails' attribute with the provided contactDetails parameter.
        self.menu = menu  # Assign the 'menu' attribute with the provided menu parameter.
        self.minGuests = minGuests  # Assign the 'minGuests' attribute with the provided minGuests parameter.
        self.maxGuests = maxGuests  # Assign the 'maxGuests' attribute with the provided maxGuests parameter.

# Function to handle GUI initialization
def main():
    # Function to add details based on selected category
    def add_details():
        # Retrieve the selected category from the GUI input
        category = category_var.get()
        # Based on the selected category, call the respective function to display information entry fields
        if category == "Employee":
            display_employee_info()
        elif category == "Client":
            display_client_info()
        elif category == "Event":
            display_event_info()
        elif category == "Guest":
            display_guest_info()
        elif category == "Venue":
            display_venue_info()
        elif category == "Caterer":
            display_caterer_info()

    # Function to display employee information
    def display_employee_info():
        # Clear any existing entries and info labels on the GUI
        clear_entries()
        clear_info_label()
        # Define the fields for employee information entry
        employee_fields = ["Name:", "Employee ID:", "Department:", "Job Title:", "Basic Salary:", "Age:",
                           "Date of Birth:", "Passport Details:"]
        # Iterate over the employee fields, creating corresponding labels and entry widgets
        for i, field in enumerate(employee_fields):
            tk.Label(info_frame, text=field).grid(row=i, column=0, sticky="e")  # Create a label for the field
            entry = tk.Entry(info_frame)  # Create an entry widget for user input
            entry.grid(row=i, column=1)  # Place the entry widget in the GUI grid
            employee_entries.append(entry)  # Add the entry widget to the list for later retrieval

    # Function to display client information
    def display_client_info():
        # Clear any existing entries and info labels on the GUI
        clear_entries()
        clear_info_label()
        # Define the fields for client information entry
        client_fields = ["Client ID:", "Name:", "Address:", "Contact Details:", "Budget:"]
        # Iterate over the client fields, creating corresponding labels and entry widgets
        for i, field in enumerate(client_fields):
            tk.Label(info_frame, text=field).grid(row=i, column=0, sticky="e")  # Create a label for the field
            entry = tk.Entry(info_frame)  # Create an entry widget for user input
            entry.grid(row=i, column=1)  # Place the entry widget in the GUI grid
            client_entries.append(entry)  # Add the entry widget to the list for later retrieval

    # Function to display event information
    def display_event_info():
        # Clear any existing entries and info labels on the GUI
        clear_entries()
        clear_info_label()
        # Define the fields for event information entry
        event_fields = ["Event ID:", "Type:", "Theme:", "Date:", "Time:", "Duration:", "Venue:", "Client:", "Guests:",
                        "Catering Company:", "Cleaning Company:", "Decorations Company:", "Entertainment Company:",
                        "Furniture Supplier:", "Invoice:"]
        # Iterate over the event fields, creating corresponding labels and entry widgets
        for i, field in enumerate(event_fields):
            tk.Label(info_frame, text=field).grid(row=i, column=0, sticky="e")  # Create a label for the field
            entry = tk.Entry(info_frame)  # Create an entry widget for user input
            entry.grid(row=i, column=1)  # Place the entry widget in the GUI grid
            event_entries.append(entry)  # Add the entry widget to the list for later retrieval

    # Function to display guest information
    def display_guest_info():
        # Clear any existing entries and info labels on the GUI
        clear_entries()
        clear_info_label()
        # Define the fields for guest information entry
        guest_fields = ["Guest ID:", "Name:", "Address:", "Contact Details:"]
        # Iterate over the guest fields, creating corresponding labels and entry widgets
        for i, field in enumerate(guest_fields):
            tk.Label(info_frame, text=field).grid(row=i, column=0, sticky="e")  # Create a label for the field
            entry = tk.Entry(info_frame)  # Create an entry widget for user input
            entry.grid(row=i, column=1)  # Place the entry widget in the GUI grid
            guest_entries.append(entry)  # Add the entry widget to the list for later retrieval

    # Function to display venue information
    def display_venue_info():
        # Clear any existing entries and info labels on the GUI
        clear_entries()
        clear_info_label()
        # Define the fields for venue information entry
        venue_fields = ["Venue ID:", "Name:", "Address:", "Contact:", "Min Guests:", "Max Guests:"]
        # Iterate over the venue fields, creating corresponding labels and entry widgets
        for i, field in enumerate(venue_fields):
            tk.Label(info_frame, text=field).grid(row=i, column=0, sticky="e")  # Create a label for the field
            entry = tk.Entry(info_frame)  # Create an entry widget for user input
            entry.grid(row=i, column=1)  # Place the entry widget in the GUI grid
            venue_entries.append(entry)  # Add the entry widget to the list for later retrieval

    # Function to display caterer information
    def display_caterer_info():
        # Clear any existing entries and info labels on the GUI
        clear_entries()
        clear_info_label()
        # Define the fields for caterer information entry
        caterer_fields = ["Caterer ID:", "Name:", "Address:", "Contact:", "Menu:", "Min Guests:", "Max Guests:"]
        # Iterate over the caterer fields, creating corresponding labels and entry widgets
        for i, field in enumerate(caterer_fields):
            tk.Label(info_frame, text=field).grid(row=i, column=0, sticky="e")  # Create a label for the field
            entry = tk.Entry(info_frame)  # Create an entry widget for user input
            entry.grid(row=i, column=1)  # Place the entry widget in the GUI grid
            caterer_entries.append(entry)  # Add the entry widget to the list for later retrieval

    # Function to save all the information
    def save_information():
        # Retrieve the selected category from the GUI input
        category = category_var.get()
        data = None
        # Based on the selected category, retrieve the data from the corresponding entry fields
        if category == "Employee":
            data = [entry.get() for entry in employee_entries]
        elif category == "Client":
            data = [entry.get() for entry in client_entries]
        elif category == "Event":
            data = [entry.get() for entry in event_entries]
        elif category == "Guest":
            data = [entry.get() for entry in guest_entries]
        elif category == "Venue":
            data = [entry.get() for entry in venue_entries]
        elif category == "Caterer":
            data = [entry.get() for entry in caterer_entries]
        # If data is retrieved successfully, save it to a file
        if data:
            try:
                with open(category.lower() + "s.dat", "rb") as file:
                    existing_data = pickle.load(file)
            except FileNotFoundError:
                existing_data = []
            existing_data.append(data)
            with open(category.lower() + "s.dat", "wb") as file:
                pickle.dump(existing_data, file)
            # Show a message box indicating successful saving of information
            messagebox.showinfo("Success", "Information saved successfully.")

    # Function to delete saved information
    def delete_information():
        categories = ["Employee", "Client", "Event", "Guest", "Venue", "Caterer"]
        # Iterate over each category and attempt to delete its corresponding file
        for category in categories:
            try:
                filename = category.lower() + "s.dat"
                os.remove(filename)  # Delete the file if it exists
            except FileNotFoundError:
                continue  # Continue to the next category if the file is not found
        # Show a message box indicating successful deletion of saved information
        messagebox.showinfo("Deleted", "Saved information has been deleted.")

    # Function to display the bill
    def display_bill():
        bill_text = ""  # Initialize an empty string to store the bill text
        categories = ["Employee", "Client", "Event", "Guest", "Venue", "Caterer"]  # Define the categories
        all_ids = {category: set() for category in
                   categories}  # Initialize a dictionary to store unique IDs for each category

        # Iterate over each category
        for category in categories:
            try:
                with open(category.lower() + "s.dat", "rb") as file:  # Open the corresponding file for each category
                    saved_data = pickle.load(file)  # Load the saved data from the file
                if saved_data:  # If there is saved data for the category
                    bill_text += "Saved {} Information:\n\n".format(
                        category)  # Add a header for the category to the bill text
                    for item in saved_data:  # Iterate over each item in the saved data
                        if isinstance(item, (list, tuple)):  # Check if the item is a list or tuple
                            for index, attribute in enumerate(item):  # Iterate over the attributes of the item
                                bill_text += "{}: {}\n".format(category.capitalize() + " Attribute " + str(index + 1),
                                                               attribute)  # Add each attribute to the bill text
                            bill_text += "\n"  # Add a newline after each item
                        else:  # If the item is not a list or tuple
                            if item not in all_ids[
                                category]:  # Check if the item ID is not already included in the bill
                                all_ids[category].add(item)  # Add the item ID to the set of IDs for the category
                                bill_text += "{}: {}\n\n".format(category.capitalize() + " ID",
                                                                 item)  # Add the item ID to the bill text
            except FileNotFoundError:  # Handle the case where the file for the category is not found
                continue  # Continue to the next category if the file is not found

        # Display the bill text in a message box
        if bill_text:  # If there is bill text
            messagebox.showinfo("Bill", bill_text)  # Show the bill text in a message box
        else:  # If there is no bill text
            messagebox.showinfo("Bill","No information found for any category.")  # Show a message indicating no information found

    # Function to clear entry fields
    def clear_entries():
        # Iterate over all entry widgets in each entry list and clear their contents
        for entry in employee_entries + client_entries + event_entries + guest_entries + venue_entries + caterer_entries:
            entry.delete(0, tk.END)  # Delete the contents of the entry widget from index 0 to the end

    # Function to clear info label
    def clear_info_label():
        # Clear the text of the info_label widget
        info_label.config(text="")

    # Create GUI and add widgets
    root = tk.Tk()
    root.title("Event Management System")

    # Dropdown menu for selecting category
    tk.Label(root, text="Select Category:").grid(row=0, column=0)
    category_var = tk.StringVar(root)
    categories = ["Employee", "Client", "Event", "Guest", "Venue", "Caterer"]
    category_menu = ttk.Combobox(root, textvariable=category_var, values=categories, state="readonly")
    category_menu.grid(row=0, column=1)

    # Add button to proceed with filling details
    add_details_btn = tk.Button(root, text="Proceed", command=add_details)
    add_details_btn.grid(row=0, column=2)

    # Frame to hold entry fields
    global info_frame
    info_frame = tk.Frame(root)
    info_frame.grid(row=1, column=0, columnspan=3)

    # Label to display information needed to be filled
    global info_label
    info_label = tk.Label(root, text="")
    info_label.grid(row=2, column=0, columnspan=3)

    # Button to save all the information
    save_btn = tk.Button(root, text="Save Information", command=save_information)
    save_btn.grid(row=3, column=0, columnspan=3)

    # Add button to delete saved information
    delete_btn = tk.Button(root, text="Delete Information", command=delete_information)
    delete_btn.grid(row=4, column=0, columnspan=3)

    # Button to display bill
    display_bill_btn = tk.Button(root, text="Display Bill", command=display_bill)
    display_bill_btn.grid(row=5, column=0, columnspan=3)

    # Lists to hold entry fields for each category
    global employee_entries, client_entries, event_entries, guest_entries, venue_entries, caterer_entries
    employee_entries = []
    client_entries = []
    event_entries = []
    guest_entries = []
    venue_entries = []
    caterer_entries = []

    root.mainloop()

if __name__ == "__main__":
    main() #Displaying the GUI Window