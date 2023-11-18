import tkinter as tk
from tkinter import messagebox
from fancify_text import 𝗌𝖺𝗇𝗌𝖲𝖾𝗋𝗂𝖿

# Create the main window
root = tk.Tk()
root.title("User Information")
root.configure(bg='khaki')

# Validation function for checking if input contains only letters and spaces
def is_valid_name(entry_name):
    return all(entry.isalpha() or entry.isspace() for entry in entry_name)

# Validation function for checking if input contains only numbers
def is_valid_age(entry_age):
    return entry_age.isdigit()

# Submit function to process user input and show a message
def submit():
    first_name = entry_firstname.get()
    middle_name = entry_middlename.get()
    surname = entry_surname.get()
    age = entry_age.get()
    address = entry_address.get()

    # Validate names
    if not all(is_valid_name(entry_text) for entry_text in (first_name, middle_name, surname)):
        messagebox.showwarning("Invalid Input", "Please enter a valid name with letters only.")
        return

    # Validate age
    if not is_valid_age(age):
        messagebox.showwarning("Invalid Input", "Please enter a valid age with numbers only.")
        return

    # Check for incomplete information
    if any(not entry.get() for entry in (entry_firstname, entry_middlename, entry_surname, entry_age, entry_address)):
        messagebox.showwarning("Incomplete Information", "Please fill in all fields.")
        return

# Clear entries after submission
    
    entry_firstname.delete(0, 'end')
    entry_middlename.delete(0, 'end')
    entry_surname.delete(0, 'end')
    entry_age.delete(0, 'end')
    entry_address.delete(0, 'end')
    
    # Show submission message
    message = f"Thanks for filling up!\n\nMy name is {first_name} {middle_name} {surname}\nI am {age} years old\nI live in {address}"
    messagebox.showinfo("Submission Successful", message )

# GUI components
label_fillup = tk.Label(root, text="Please fill-up the info below!:", font=("Bold", 20,), fg='brown', bg="khaki")
label_fillup.grid(row=0, column=0, columnspan=2)

label_firstname = tk.Label(root, text="Enter your First name:", font=(sansSerif, 15), bg="khaki")
label_firstname.grid(row=1, column=0, padx=10, pady=5)

label_middlename = tk.Label(root, text="Enter your Middle name:", font=(sansSerif, 15), bg="khaki")
label_middlename.grid(row=2, column=0, padx=10, pady=5)

label_surname = tk.Label(root, text="Enter your Surname:", font=(sansSerif, 15), bg="khaki")
label_surname.grid(row=3, column=0, padx=10, pady=5)

label_age = tk.Label(root, text="Enter your Age:", font=(sansSerif, 15), bg="khaki")
label_age.grid(row=4, column=0, padx=10, pady=5)

label_address = tk.Label(root, text="Enter your complete Address:", font=(sansSerif, 15,), bg="khaki")
label_address.grid(row=5, column=0, padx=10, pady=5)

entry_firstname = tk.Entry(root, font=(sansSerif, 15))
entry_firstname.grid(row=1, column=1, padx=10)

entry_middlename = tk.Entry(root, font=(sansSerif, 15))
entry_middlename.grid(row=2, column=1, padx=10)

entry_surname = tk.Entry(root, font=(sansSerif, 15))
entry_surname.grid(row=3, column=1, padx=10)

entry_age = tk.Entry(root, font=(sansSerif, 15))
entry_age.grid(row=4, column=1, padx=10)

entry_address = tk.Entry(root, font=(sansSerif, 15))
entry_address.grid(row=5, column=1, padx=10)

submit_button = tk.Button(root, text="Submit", command=submit, font=(sansSerif, 18), bg="yellow")
submit_button.grid(row=6, columnspan=2, padx=10, pady=10, sticky="ew")

root.mainloop()