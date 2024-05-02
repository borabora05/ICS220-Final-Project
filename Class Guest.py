class Guest:  # Define a class named Guest

    def __init__(self, guestID, name, address, contactDetails):
        # Constructor method to initialize the Guest object with provided attributes.

        self.guestID = guestID  # Assign the 'guestID' attribute with the provided guestID parameter.
        self.name = name  # Assign the 'name' attribute with the provided name parameter.
        self.address = address  # Assign the 'address' attribute with the provided address parameter.
        self.contactDetails = contactDetails  # Assign the 'contactDetails' attribute with the provided contactDetails parameter.

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
