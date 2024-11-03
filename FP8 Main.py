import sqlite3
import tkinter as tk
from tkinter import messagebox

# Database creation
conn = sqlite3.connect('customer_feedback.db')  # Connect to the database
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS feedback
             (name TEXT, email TEXT, message TEXT)''')  # Create table if it doesn't exist
conn.commit()

# GUI design
def submit_feedback():

    # Get input data from GUI fields, store it in the database, and show a confirmation message
    name = entry_name.get()
    email = entry_email.get()
    message = entry_message.get("1.0", tk.END)

    # Insert data into the database
    c.execute("INSERT INTO feedback VALUES (?, ?, ?)", (name, email, message)) 
    conn.commit()
    messagebox.showinfo("Feedback Submitted", "Thank you for your feedback!")

    # Clear the fields after submitting
    entry_name.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_message.delete("1.0", tk.END)

def print_feedback():

    # Prompt for a password in the console and print all feedback entries if the password is correct.
    password = input("Enter password to view feedback: ")
    if password == 'BradsPassword':
        c.execute("SELECT * FROM feedback")
        for row in c.fetchall():
            print(row)
    else:
        print("Access denied: incorrect password.")  # Deny access if password is incorrect

# Main GUI window
root = tk.Tk()
root.title("Customer Feedback")

# GUI Labels and input fields
tk.Label(root, text="Name").grid(row=0, column=0, columnspan=2)
tk.Label(root, text="Email").grid(row=1, column=0, columnspan=2)
tk.Label(root, text="Feedback").grid(row=2, column=0, columnspan=2)

# Entry areas for name and email, as well as text area for the feedback message.
entry_name = tk.Entry(root)
entry_email = tk.Entry(root)
entry_message = tk.Text(root, height=4, width=40)

# Positioning input fields on the grid
entry_name.grid(row=0, column=2, padx=10)
entry_email.grid(row=1, column=2, padx=10)
entry_message.grid(row=2, column=2, padx=10)

# Frame for buttons
button_frame = tk.Frame(root)
button_frame.grid(row=3, column=2)

# Submit and Show Feedback buttons
tk.Button(button_frame, text="Submit", command=submit_feedback).grid(row=0, column=0, pady=5)
tk.Button(button_frame, text="Show Feedback", command=print_feedback).grid(row=1, column=0, pady=5)

root.mainloop()
