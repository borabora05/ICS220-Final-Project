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

def display_event_info():
    # Clear any existing entries and info labels on the GUI
    clear_entries()
    clear_info_label()
    # Define the fields for event information entry
    event_fields = ["Event ID:", "Type:", "Theme:", "Date:", "Time:", "Duration:", "Venue:", "Client:", "Guests:", "Catering Company:", "Cleaning Company:", "Decorations Company:", "Entertainment Company:", "Furniture Supplier:", "Invoice:"]
    # Iterate over the event fields, creating corresponding labels and entry widgets
    for i, field in enumerate(event_fields):
        tk.Label(info_frame, text=field).grid(row=i, column=0, sticky="e")  # Create a label for the field
        entry = tk.Entry(info_frame)  # Create an entry widget for user input
        entry.grid(row=i, column=1)  # Place the entry widget in the GUI grid
        event_entries.append(entry)  # Add the entry widget to the list for later retrieval
