import re

class System:

    def __init__(self):
        self.contacts = {}
        self.menu()

    # mini project task 1
    def menu(self):    
        print('''Welcome to the Contact Management System!
              Menu:
              1. Add a new contact
              2. Edit an existing contact
              3. Delete a contact
              4. Search for a contact
              5. Display all contacts
              6. Export contact to a text file
              7. Quit''')
        
    # mini project task 2

    def add_contact(self):

        email = input("Enter email address of the contact you would like to add: ")

        if email in self.contacts:
            print("The email entered is already associated with another account.")
            return
        name = input("Enter the name of this contact: ")
        phone = input("Enter the phone number for this contact: ")
        info = input("Enter any additional information for this contact: ")

        self.contacts[email] = {
            'Name' : name,
            'Phone Number' : phone,
            'Additional Information' : info
        }
        print("Contact added successfully.")
    
    def edit_contact(self):
        try: 
            email = input("Enter the email of the contact you would like to edit: ")

            if email in self.contacts:
                name = input("Enter the new name for this contact or press enter if no change needs to be made") or self.contacts[email]['Name']
                phone = input("Enter the new phone number for this contact or press enter if no change needs to be made") or self.contacts[email]['Phone Number']
                info = input("Enter information you would like to add to this contact or press enter if no change needs to be made") or self.contacts[email]['Additional Information']

                self.contacts[email] = {
                    'Name' : name,
                    'Phone Number' : phone, 
                    'Additional Information' : info
                }

                print("This contact has been edited successfully.")

        except Exception as e:
            print(f"An unexpected error has occurred: {e}")

    
    def delete_contact(self):
        try:
            email = input("Enter the email of the contact you would like to delete: ")

            if email in self.contacts:
                del self.contacts[email]
                print("Contact has been successfully deleted.")
            
            else:
                print("Contact not found")

        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    
    def search_contact(self):
        try:
            email = input("Enter the email associated with the contact you are looking for: ")

            if email in self.contacts:
                contact = self.contacts[email]

                print(f"Name: {contact['Name']}, Phone Number: {contact['Phone Number']}, Additional Information: {contact['Additional Information']}")

            else:
                print("Contact not found.")

        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    
    def display_contacts(self):
        try: 
            if self.contacts:
                for email, information in self.contacts.items():
                    print(f"Name: {information['Name']}, Email: {email}, Phone Number: {information['Phone Number']}, Additional Information: {information['Additional Information']}")

            else:
                print(f"No contacts to display.")
        
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
    
    def export_contacts(self):
        try:
            file_name = input("Enter the name you would like for the file you are exporting your contacts to: ")

            with open(file_name, 'w') as file:
                for email, information in self.contacts.items():
                    data = f"Name: {information['Name']}, Email: {email}, Phone Number: {information['Phone Number']}, Additional Information: {information['Additional Information']}"

                    file.write(data)
                print("Contacts exported successfully.")
        except IOError as e:
            print(f"An error occurred: {e}")


    # mini project task 4
    def valid_email(self, email):
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(email_regex, email)
    
    def valid_phone_number(self, phone):
        phone_regex = r'^\+?\d{10,15}$'
        return re.match(phone_regex, phone)
    

    def main(self):
        while True:
                choice = input("What what you like to do? (Choose an option 1-7): ")

                if choice == '1':
                    self.add_contact()
                elif choice =='2':
                    self.edit_contact()
                elif choice =='3':
                    self.delete_contact()
                elif choice == '4':
                    self.search_contact()
                elif choice == '5':
                    self.display_contacts()
                elif choice == '6':
                    self.export_contacts()
                elif choice == '7':
                    print("Quitting the Contact Management System. Bye!")
                    break
                else:
                    print("That is not a valid option choice, please choose a number between 1 and 7.")


if __name__ == "__main__":
    system = System()
    system.main()



            
