import tkinter as tk
from tkinter import messagebox, simpledialog
import csv

class ContactBookApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Emmanuel Phone Book")
        self.master.geometry("720x400")  # Set window size to 720x400
        self.master.configure(bg="#f0f0f0")  # Set background color
        # Set the icon for the application window
        self.master.iconbitmap("./myicon.ico")  # Replace "path/to/icon.ico" with the path to your icon file
        
        self.contacts = []
        self.load_contacts_from_file()  # Load contacts from CSV file
        
        self.create_widgets()
        
    def create_widgets(self):
        # Frame to hold input fields
        input_frame = tk.Frame(self.master, bg="#f0f0f0")
        input_frame.pack(pady=20)

        # Labels and entry fields
        tk.Label(input_frame, text="Name:", font=("Segoe UI", 12), bg="#f0f0f0").grid(row=0, column=0, sticky="e", padx=10, pady=5)
        self.name_entry = tk.Entry(input_frame, font=("Segoe UI", 12))
        self.name_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(input_frame, text="Phone Number:", font=("Segoe UI", 12), bg="#f0f0f0").grid(row=1, column=0, sticky="e", padx=10, pady=5)
        self.phone_entry = tk.Entry(input_frame, font=("Segoe UI", 12))
        self.phone_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(input_frame, text="Email:", font=("Segoe UI", 12), bg="#f0f0f0").grid(row=2, column=0, sticky="e", padx=10, pady=5)
        self.email_entry = tk.Entry(input_frame, font=("Segoe UI", 12))
        self.email_entry.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(input_frame, text="Address:", font=("Segoe UI", 12), bg="#f0f0f0").grid(row=3, column=0, sticky="e", padx=10, pady=5)
        self.address_entry = tk.Entry(input_frame, font=("Segoe UI", 12))
        self.address_entry.grid(row=3, column=1, padx=10, pady=5)
            
        # Buttons
        # Add Contact button
        button_style = {"font": ("Segoe UI", 12), "width": 15}
        
        add_contact_button = tk.Button(self.master, text="Add Contact", command=self.add_contact, bg="#4CAF50", fg="white", **button_style)
        add_contact_button.pack(pady=10)



        # Center the Add Contact button - this is not needed again
        # add_contact_button.place(anchor=tk.CENTER)

        view_update_frame = tk.Frame(self.master, bg="#f0f0f0")
        view_update_frame.pack(pady=10)
        tk.Button(view_update_frame, text="View Contacts", command=self.view_contacts, bg="#4CAF50", fg="white", **button_style).pack(side=tk.LEFT, padx=10)
        tk.Button(view_update_frame, text="Update Contact", command=self.update_contact, bg="#4CAF50", fg="white", **button_style).pack(side=tk.LEFT, padx=10)

        search_delete_frame = tk.Frame(self.master, bg="#f0f0f0")
        search_delete_frame.pack(pady=10)
        tk.Button(search_delete_frame, text="Search Contact", command=self.search_contact, bg="#4CAF50", fg="white", **button_style).pack(side=tk.LEFT, padx=10)
        tk.Button(search_delete_frame, text="Delete Contact", command=self.delete_contact, bg="#FF5733", fg="white", **button_style).pack(side=tk.LEFT, padx=10)

       
    
    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()
        
        contact = {"Name": name, "Phone": phone, "Email": email, "Address": address}
        self.contacts.append(contact)
        
        self.save_contacts_to_file()  # Save contacts to CSV file
        
        messagebox.showinfo("Success", "Contact added successfully!")
        
        self.clear_entries()
    
    def view_contacts(self):
        if not self.contacts:
            messagebox.showinfo("No Contacts", "There are no contacts to display.")
        else:
            contacts_str = ""
            for idx, contact in enumerate(self.contacts, start=1):
                contacts_str += f"{idx}. Name: {contact['Name']}, Phone: {contact['Phone']}\n"
            messagebox.showinfo("Contacts", contacts_str)
    
    def search_contact(self):
        search_term = simpledialog.askstring("Search", "Enter name or phone number to search:")
        if search_term:
            found_contacts = [contact for contact in self.contacts if search_term.lower() in contact['Name'].lower() or search_term in contact['Phone']]
            if found_contacts:
                contacts_str = ""
                for idx, contact in enumerate(found_contacts, start=1):
                    contacts_str += f"{idx}. Name: {contact['Name']}, Phone: {contact['Phone']}\n"
                messagebox.showinfo("Search Results", contacts_str)
            else:
                messagebox.showinfo("No Results", "No contacts found matching the search criteria.")
    
    def update_contact(self):
        index = simpledialog.askinteger("Update", "Enter the index of the contact to update:") - 1
        if index is not None and 0 <= index < len(self.contacts):
            name = self.name_entry.get()
            phone = self.phone_entry.get()
            email = self.email_entry.get()
            address = self.address_entry.get()
            
            self.contacts[index] = {"Name": name, "Phone": phone, "Email": email, "Address": address}
            self.save_contacts_to_file()  # Save contacts to CSV file
            messagebox.showinfo("Success", "Contact updated successfully!")
            self.clear_entries()
        else:
            messagebox.showinfo("Invalid Index", "Please enter a valid index.")
    
    def delete_contact(self):
        index = simpledialog.askinteger("Delete", "Enter the index of the contact to delete:") - 1
        if index is not None and 0 <= index < len(self.contacts):
            del self.contacts[index]
            self.save_contacts_to_file()  # Save contacts to CSV file
            messagebox.showinfo("Success", "Contact deleted successfully!")
        else:
            messagebox.showinfo("Invalid Index", "Please enter a valid index.")
    
    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)
    
    def load_contacts_from_file(self):
        try:
            with open("contacts.csv", mode="r", newline="") as file:
                reader = csv.DictReader(file)
                self.contacts = [row for row in reader]
        except FileNotFoundError:
            pass  # If file doesn't exist, no contacts to load
    
    def save_contacts_to_file(self):
        with open("contacts.csv", mode="w", newline="") as file:
            fieldnames = ["Name", "Phone", "Email", "Address"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(self.contacts)

def main():
    root = tk.Tk()
    app = ContactBookApp(root)
    # Center window on screen
    window_width = root.winfo_reqwidth()
    window_height = root.winfo_reqheight()
    position_right = int(root.winfo_screenwidth()/2 - window_width/2)
    position_down = int(root.winfo_screenheight()/2 - window_height/2)
    root.geometry("+{}+{}".format(position_right, position_down))
    root.mainloop()

if __name__ == "__main__":
    main()
