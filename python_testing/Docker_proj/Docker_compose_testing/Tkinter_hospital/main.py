import tkinter as tk
from tkinter import ttk,messagebox
import mysql.connector
from mysql.connector import Error

# Initialize a dictionary to hold the input field references dynamically
input_fields = {}

def clear_input_fields():
    """Clear the input fields in the GUI."""
    for widget in input_frame.winfo_children():
        widget.destroy()
    global input_fields
    input_fields = {}  # Reinitialize the dictionary after clearing

def update_input_fields(*args):
    """Update input fields based on the selection (Doctors or Patients)."""
    clear_input_fields()  # First, clear existing fields
    selection = search_option.get().lower()

    # Labels and Entries for Doctors and Patients
    common_labels_entries = {
        "first_name": "First Name",
        "last_name": "Last Name",
        "date_of_birth": "Date of Birth (YYYY-MM-DD)",
        "age": "Age",
        "gender": "Gender",
        "contact_info": "Contact Info"
    }

    if selection == "doctors":
        specific_labels_entries = {
            "specialty": "Specialty",
            "date_of_hire": "Date of Hire (YYYY-MM-DD)",
            "hours_worked": "Hours Worked"
        }
    elif selection == "patients":
        specific_labels_entries = {
            "weight": "Weight (kg)",
            "height": "Height (m)",
            "reason_for_visit": "Reason for Visit",
            "current_diagnosis": "Current Diagnosis",
            "medical_history": "Medical History",
            "allergies": "Allergies"
        }
    else:
        print("Invalid table selection")
        return

    # Combine common and specific fields for the selected option
    all_labels_entries = {**common_labels_entries, **specific_labels_entries}

    # Dynamically generate label and entry widgets
    for i, (field, label) in enumerate(all_labels_entries.items(), start=1):
        ttk.Label(input_frame, text=label).grid(row=i, column=0, padx=5, pady=2, sticky="w")
        entry_widget = ttk.Entry(input_frame)
        entry_widget.grid(row=i, column=1, padx=5, pady=2, sticky="ew")
        input_fields[field] = entry_widget  # Store entry widget for later access

def load_database_entries():
    """Load and display database entries for selected table."""
    table_name = search_option.get().lower()
    query = f"SELECT first_name, last_name FROM {table_name}"
    connection = None
    try:
        connection = mysql.connector.connect(
            host='mysql',  # Adjust as necessary for your setup
            database='imagedb',
            user='user',
            password='password'
        )
        cursor = connection.cursor()
        cursor.execute(query)
        records = cursor.fetchall()

        entries_listbox.delete(0, tk.END)
        for row in records:
            entries_listbox.insert(tk.END, f"{row[0]} {row[1]}")
    except Error as e:
        print("Error reading data from MySQL table", e)
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()

def upload_data():
    """Upload data from input fields to the selected table."""
    table_name = search_option.get().lower()
    connection = None  # Initialize connection here
    
    # Prepare the data and query based on the table_name
    try:
        fields = ', '.join(input_fields.keys())
        placeholders = ', '.join(['%s'] * len(input_fields))
        query = f"INSERT INTO {table_name} ({fields}) VALUES ({placeholders})"
        data = tuple(field.get() for field in input_fields.values())

        connection = mysql.connector.connect(
            host='mysql',  # Adjust as necessary for your setup
            database='imagedb',
            user='user',
            password='password'
        )
        
        cursor = connection.cursor()
        cursor.execute(query, data)
        connection.commit()
        print("Data uploaded successfully.")
        load_database_entries()  # Optionally refresh the list after insertion
    except Error as e:
        print(f"Error inserting data into MySQL table: {e}")
    finally:
        if connection is not None and connection.is_connected():
            cursor.close()
            connection.close()


# Initialize the main application window
app = tk.Tk()
app.title("Medical Database Entries")
app.geometry("800x600")

# Define frames
search_frame = ttk.Frame(app)
search_frame.pack(pady=10, fill='x')

input_frame = ttk.Frame(app)
input_frame.pack(pady=20, fill="x", expand=True)

entries_frame = ttk.Frame(app)
entries_frame.pack(fill="both", expand=True, padx=10)

# Define and pack the search option combobox
search_option = ttk.Combobox(search_frame, values=["Doctors", "Patients"], width=20)
search_option.current(0)
search_option.grid(row=0, column=0, padx=10, sticky='ew')
search_option.bind('<<ComboboxSelected>>', update_input_fields)

# Define and pack the load entries button
load_button = ttk.Button(search_frame, text="Load Entries", command=load_database_entries)
load_button.grid(row=0, column=1, padx=10, sticky='ew')

# Place the upload data button beside the load entries button within the search_frame
upload_button = ttk.Button(search_frame, text="Upload Data", command=upload_data)
upload_button.grid(row=0, column=2, padx=10, sticky='ew')

# Configure the entries listbox and scrollbar
entries_listbox = tk.Listbox(entries_frame, width=50, height=20)
entries_listbox.pack(side="left", fill="both", expand=True)

scrollbar = ttk.Scrollbar(entries_frame, orient="vertical", command=entries_listbox.yview)
scrollbar.pack(side="right", fill="y")
entries_listbox.configure(yscrollcommand=scrollbar.set)

# Initially update input fields based on the default selection
update_input_fields()

# Start the Tkinter event loop
app.mainloop()

