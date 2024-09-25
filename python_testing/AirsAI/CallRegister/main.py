import tkinter as tk
from datetime import datetime

# Function to start the timer
def start_timer():
    global start_time
    start_time = datetime.now()

# Function to format the elapsed time
def format_time(elapsed_time):
    minutes, seconds = divmod(elapsed_time.seconds, 60)
    return f"{minutes}:{seconds:02d}"

# Function to log the selected tag with the current timestamp
def log_issue(tag):
    elapsed_time = datetime.now() - start_time
    formatted_time = format_time(elapsed_time)
    log_entry = f"{formatted_time} {tag}\n"
    
    # Insert the log entry at the top of the log box
    log_box.insert("1.0", log_entry)

# Initialize the main window
root = tk.Tk()
root.title("Call Quality Logger")

# Set the window size and make it resizable
root.geometry("400x300")
root.attributes("-topmost", True)  # Always on top
root.resizable(True, True)  # Make the window resizable

# Start the timer when the window opens
start_timer()

# List of tags
tags = [
    "Total silence", 
    "Bot interrupted", 
    "Bot paused", 
    "Bot stuttered", 
    "Driver couldn't hear the bot", 
    "Driver is not audible", 
    "Call dropped suddenly", 
    "Bot didn’t hang up", 
    "Static", 
    "Echo"
]

# Create buttons for each tag
for tag in tags:
    button = tk.Button(root, text=tag, command=lambda t=tag: log_issue(t))
    button.pack(fill=tk.X)

# Create a text box to display the log
log_box = tk.Text(root, height=15, width=50)
log_box.pack()

# Run the GUI event loop
root.mainloop()
