import tkinter as tk
from tkinter import ttk
import mysql.connector
from mysql.connector import Error

def load_database_entries():
    table_name = search_option.get().lower()  # 'Doctors' or 'Patients'
    query = f"SELECT first_name, last_name FROM {table_name}"
    try:
        connection = mysql.connector.connect(
            host='mysql',  # Adjust as necessary - if you're on a local machine use localhost
            database='imagedb',  # Your database name
            user='user',  # Your database user
            password='password'  # Your database password
        )
        cursor = connection.cursor()
        cursor.execute(query)
        records = cursor.fetchall()
        
        # Clear the Listbox before adding new entries
        entries_listbox.delete(0, tk.END)
        
        # Inserting records into the Listbox
        for row in records:
            entries_listbox.insert(tk.END, f"{row[0]} {row[1]}")
    except Error as e:
        print("Error reading data from MySQL table", e)
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()

# Tkinter GUI setup
app = tk.Tk()
app.title("Medical Database Entries")
app.geometry("800x400")

search_frame = ttk.Frame(app)
search_frame.pack(pady=20)

search_option = ttk.Combobox(search_frame, values=["Doctors", "Patients"])
search_option.current(0)
search_option.grid(row=0, column=0, padx=10)

load_button = ttk.Button(search_frame, text="Load", command=load_database_entries)
load_button.grid(row=0, column=2, padx=10)

entries_frame = ttk.Frame(app)
entries_frame.pack(fill="both", expand=True)

entries_listbox = tk.Listbox(entries_frame, width=50, height=20)
entries_listbox.pack(side="left", fill="both", expand=True)

scrollbar = ttk.Scrollbar(entries_frame, orient="vertical", command=entries_listbox.yview)
scrollbar.pack(side="right", fill="y")

entries_listbox.configure(yscrollcommand=scrollbar.set)

app.mainloop()