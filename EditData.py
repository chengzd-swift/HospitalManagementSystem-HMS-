import re

#Done by (Kan Lap Hoe, 2300123) on 29/04/2024

def validate_input(input_prompt, pattern):
    #If the user key in the wrong format of the patient ID (e.g. B002), an error message will be shown
    while True:
        user_input = input(input_prompt)
        if re.match(pattern, user_input):
            return user_input
        else:
            print("Invalid input format. Please try again.")

def EditPatient(ws1, wb, data_file):
    #Validate and retrieve the patient ID to be edited
    patient_id = validate_input("Enter the ID of the patient you want to edit (e.g., P001): ", r'^P\d{3}$')

    found_patient = False #Initialize the variable 'found_patient' = False

    #Iterate over each row in the worksheet to find the specified patient ID
    for row in ws1.iter_rows(min_row=2, max_row=ws1.max_row, values_only=False):
        if row[0].value == patient_id:
            found_patient = True

            # Print existing details
            print("\nExisting Details:")
            print("Name:", row[1].value)
            print("Address:", row[2].value)
            print("Phone Number:", row[3].value)
            print("Emergency Contact Name:", row[4].value)
            print("Emergency Contact:", row[5].value)
            print("Allergic to Medicine:", row[6].value)
            print("History of Sickness:", row[7].value)
            print()

            # Prompt the user to update patient details
            row[1].value = validate_input("Enter new name: ", r'^[a-zA-Z\s]+$')
            row[2].value = validate_input("Enter new address, city, state, zipcode: ", r'^[\w\s,.]+$')
            row[3].value = validate_input("Enter new phone number (XXX-XXX-XXXX): ", r'^\d{3}-\d{3}-\d{4}$')
            row[4].value = validate_input("Enter new emergency contact name: ", r'^[a-zA-Z\s]+$')
            row[5].value = validate_input("Enter new emergency contact (XXX-XXX-XXXX): ", r'^\d{3}-\d{3}-\d{4}$')
            row[6].value = validate_input("Update allergy status (Y/N): ", r'^[YyNn]$')
            row[7].value = validate_input("Update history of sickness: ", r'^[\w\s]+$')

            # Save and update the updated workbook 
            wb.save(data_file)
            print()
            print("Patient details updated successfully.")
            print()
            break

    #If patient ID is not found in the worksheet
    if not found_patient:
        print()
        print("Patient ID not found. Please try again.")
        print()

# Example usage:
# Assuming ws1, wb, and data_file are properly defined and initialized
# EditPatient(ws1, wb, data_file)
