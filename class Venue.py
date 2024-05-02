class Venue:  # Define a class named Venue

    def __init__(self, venueID, name, address, contact, minGuests, maxGuests):
        # Constructor method to initialize the Venue object with provided attributes.

        self.venueID = venueID  # Assign the 'venueID' attribute with the provided venueID parameter.
        self.name = name  # Assign the 'name' attribute with the provided name parameter.
        self.address = address  # Assign the 'address' attribute with the provided address parameter.
        self.contact = contact  # Assign the 'contact' attribute with the provided contact parameter.
        self.minGuests = minGuests  # Assign the 'minGuests' attribute with the provided minGuests parameter.
        self.maxGuests = maxGuests  # Assign the 'maxGuests' attribute with the provided maxGuests parameter.

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
