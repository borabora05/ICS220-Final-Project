class Client:  # Define a class named Client

    def __init__(self, clientID, name, address, contactDetails, budget):
        # Constructor method to initialize the Client object with provided attributes.

        self.clientID = clientID  # Assign the 'clientID' attribute with the provided clientID parameter.
        self.name = name  # Assign the 'name' attribute with the provided name parameter.
        self.address = address  # Assign the 'address' attribute with the provided address parameter.
        self.contactDetails = contactDetails  # Assign the 'contactDetails' attribute with the provided contactDetails parameter.
        self.budget = budget  # Assign the 'budget' attribute with the provided budget parameter.

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
