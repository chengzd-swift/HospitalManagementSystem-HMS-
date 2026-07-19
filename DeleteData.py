def DeletePatient(ws1, wb, data_file):

    # Done by (Chew Yan Yu, 2206970) on 29/04/2024
    
    # Prompt user to input the patient ID to be deleted
    patient_id = input("Enter the patient ID that needs to be deleted: ")
    
    # Initialize a flag to track if the patient is found
    found = False 

    # Iterate through each row in the specified worksheet (ws1)
    # to find the row containing the patient ID
    for row in ws1.iter_rows(min_row=2, max_row=ws1.max_row, min_col=1, max_col=1):
        for cell in row:
            # Check if the cell value matches the input patient ID
            if str(cell.value) == patient_id:
                # Store the row number where the patient is found
                patient_row = cell.row
                # Set the flag to indicate that the patient is found
                found = True
                break  # Exit the inner loop once the patient is found

    # If the patient is found
    if found:
        print()
        print("Patient details to be deleted:")
        # Print details of the patient to be deleted
        for cell in ws1[patient_row]:
            print(cell.value)

        print()
        # Prompt user to confirm the deletion
        confirmation = input("Are you sure you want to delete this patient? (Yes/No): ").lower()

        # If user confirms the deletion
        if confirmation == "yes":
            # Delete the entire row containing the patient data
            ws1.delete_rows(patient_row)
            # Save the workbook to persist the changes
            wb.save(data_file)
            # Print a success message
            print(f"Patient with ID {patient_id} has been deleted successfully.")
            print()
        else:
            # If user cancels the deletion
            print("Patient deletion cancelled.")
            print()
    else:
        # If no patient is found with the provided ID
        print(f"No patient found with ID: {patient_id}.")
        print()


