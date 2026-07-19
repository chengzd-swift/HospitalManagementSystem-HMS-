import re

#Done by (Kan Lap Hoe, 2300123) on 29/04/2024

def AddPatient(ws1, wb, data_file):
    def validate_input(input_prompt, pattern):

        #If the user enter the wrong format like (B001). The system will display a message and prompt the user to try again
        while True:
            user_input = input(input_prompt)
            if re.match(pattern, user_input):
                return user_input
            else:
                print("Invalid input format. Please try again.")
                
    ID = validate_input("Enter patient ID (e.g., P001): ", r'^P\d{3}$')

    #If the patient ID already exists. A display message will be shown and prompt the user to enter another ID
    while True:
        if any(ID == cell.value for cell in ws1["A"]): 
            print("Patient ID already exists. Please choose another.")
            ID = validate_input("Enter patient ID (e.g., P001): ", r'^P\d{3}$')
        else:
            break
        
    #Input validation. Patient's information will only append into excel file if they provide the correct format
    name = validate_input("Enter patient name: ", r'^[a-zA-Z\s]+$')
    address = validate_input("Enter patient address, city, state, zipcode: ", r'^[\w\s,.]+$')
    phone_number = validate_input("Enter patient phone number (XXX-XXX-XXXX): ", r'^\d{3}-\d{3}-\d{4}$')
    emergency_name = validate_input("Enter emergency name: ", r'^[a-zA-Z\s]+$')
    emergency_contact = validate_input("Enter emergency contact (XXX-XXX-XXXX): ", r'^\d{3}-\d{3}-\d{4}$')
    allergic_med = validate_input("Enter if you have allergic to medicine (Y/N): ", r'^[YyNn]$')
    history_sick = validate_input("Enter your history of sickness: ", r'^[\w\s]+$')

    #Append all the patient's information into their respective column in Excel file
    ws1.append([ID, name, address, phone_number, emergency_name, emergency_contact, allergic_med, history_sick])
    wb.save(data_file)
    print("Patient details added successfully.")
    print()

# Example usage:
# Assuming ws1, wb, and data_file are properly defined and initialized
# AddPatient(ws1, wb, data_file)
