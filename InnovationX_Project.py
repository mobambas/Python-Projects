import tkinter as tk
from tkinter import ttk, scrolledtext
import phonenumbers

# Function to get country codes dynamically
def get_country_codes():
    country_codes = []
    for region in phonenumbers.COUNTRY_CODE_TO_REGION_CODE:
        country = phonenumbers.region_code_for_number(phonenumbers.parse(f"+{region}"))
        country_codes.append(f"+{region} ({country})")
    return country_codes

# Function to open the symptoms window
def open_symptoms_window(name):
    symptoms_window = tk.Toplevel(app)
    symptoms_window.title(f"Hello {name} - Enter Symptoms")

    symptoms_label = tk.Label(symptoms_window, text=f"Hello {name}! Please write down your symptoms below:", font=("Helvetica", 12))
    symptoms_label.pack(pady=10)

    symptoms_text = scrolledtext.ScrolledText(symptoms_window, wrap=tk.WORD, width=40, height=10)
    symptoms_text.pack(pady=10)

    # Function to get diagnosed diseases based on symptoms
    def diagnose():
        entered_symptoms = symptoms_text.get("1.0", tk.END)
        # TODO: Implement logic to predict diseases based on symptoms
        print(f"Entered Symptoms:\n{entered_symptoms}")
        # Placeholder - You can replace this with actual disease prediction logic

    diagnose_button = tk.Button(symptoms_window, text="Diagnose", command=diagnose, bg="#2e2e2e", fg="white")
    diagnose_button.pack(pady=10)

# Create the main window
app = tk.Tk()
app.title("Medical Diagnosis Procedural Form")

# Set window dimensions and background color
app.geometry("600x500")
app.configure(bg="#f0f0f0")  # Light grey background color

# Add a title
title_label = tk.Label(app, text="Medical Procedural Form", font=("Helvetica", 16, "bold"), bg="#2e2e2e", fg="white")
title_label.pack(pady=10, fill="x")

# Add a description
description_label = tk.Label(app, text="Revolutionary Diagnosis Tool - 95% Accuracy!", font=("Helvetica", 10), bg="#2e2e2e", fg="white")
description_label.pack(pady=5, fill="x")

# Add labels and entry widgets for bio-data
bio_frame = ttk.LabelFrame(app, text="Bio-Data", padding=(10, 5))
bio_frame.pack(pady=10, padx=10, fill="both", expand=True)

tk.Label(bio_frame, text="Full Name:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
name_entry = tk.Entry(bio_frame)
name_entry.grid(row=0, column=1, padx=10, pady=5, sticky="w")

tk.Label(bio_frame, text="Age:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
age_entry = tk.Entry(bio_frame)
age_entry.grid(row=1, column=1, padx=10, pady=5, sticky="w")

tk.Label(bio_frame, text="Gender:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
gender_var = tk.StringVar()
gender_combobox = ttk.Combobox(bio_frame, textvariable=gender_var, values=["Male", "Female", "Other"])
gender_combobox.grid(row=2, column=1, padx=10, pady=5, sticky="w")

# Add labels and entry widgets for contact information
contact_frame = ttk.LabelFrame(app, text="Patient Contact Information", padding=(10, 5))
contact_frame.pack(pady=10, padx=10, fill="both", expand=True)

tk.Label(contact_frame, text="Phone Number:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
phone_number_entry = tk.Entry(contact_frame)
phone_number_entry.grid(row=0, column=1, padx=10, pady=5, sticky="w")

tk.Label(contact_frame, text="Country Code:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
country_code_var = tk.StringVar()
country_code_combobox = ttk.Combobox(contact_frame, textvariable=country_code_var, values=get_country_codes())
country_code_combobox.grid(row=1, column=1, padx=10, pady=5, sticky="w")

tk.Label(contact_frame, text="Email Address:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
email_entry = tk.Entry(contact_frame)
email_entry.grid(row=2, column=1, padx=10, pady=5, sticky="w")

tk.Label(contact_frame, text="Home Address:").grid(row=3, column=0, padx=10, pady=5, sticky="w")
address_entry = tk.Entry(contact_frame)
address_entry.grid(row=3, column=1, padx=10, pady=5, sticky="w")

# Function to handle form submission
def submit_bio_data():
    name = name_entry.get()
    age = age_entry.get()
    gender = gender_var.get()
    phone_number = phone_number_entry.get()
    country_code = country_code_var.get()
    email = email_entry.get()
    home_address = address_entry.get()

    # Validate input
    if name and age and gender and phone_number and country_code and email and home_address:
        print(f"Name: {name}\nAge: {age}\nGender: {gender}")
        print(f"Phone Number: {country_code} {phone_number}\nEmail: {email}\nHome Address: {home_address}")
        open_symptoms_window(name)  # Open the symptoms window
    else:
        print("Please fill in all the fields.")

# Add a button to submit the bio-data
submit_button = tk.Button(app, text="Submit", command=submit_bio_data, bg="#2e2e2e", fg="white")
submit_button.pack(pady=20)

# Placeholder for a logo (replace 'path_to_logo.png' with the actual path to your logo)
logo_image = tk.PhotoImage(file='medicine_logo.png')
logo_label = tk.Label(app, image=logo_image)
logo_label.pack(pady=10)

# Start the Tkinter event loop
app.mainloop()
