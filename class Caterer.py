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
