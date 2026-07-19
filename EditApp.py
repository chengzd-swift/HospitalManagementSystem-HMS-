import re

#Done by (Cheng Zheng De, 2207492) on 29/04/2024

def EditAppointment(ws2, wb, data_file):
    def validate_input(input_prompt, validation_pattern):
        while True:
            user_input = input(input_prompt)
            if re.match(validation_pattern, user_input):
                return user_input
            else:
                print("Invalid input format. Please try again.")

    patient_id = input("Enter the ID of the patient you want to edit: ")

    # Initialize a counter to track the row index
    row_index = 1

    for row in ws2.iter_rows(values_only=True):
        if row[2] == patient_id:  # Assuming ID is in the first column
            # Print existing details
            print()
            print("Existing Details:")
            print("Date:", row[0])
            print("Time:", row[1])
            print("Patient ID:", row[2])
            print("Patient Name:", row[3])
            print("Sickness:", row[4])
            print("Medicine:", row[5])
            print("Total: RM", row[6])
            print("Next appointment:", row[7])
            print("Next appointment date:", row[8])
            print("Remarks:", row[9])
            print()

            # Update details
            new_date = validate_input("Enter a date for appointment (YYYY-MM-DD): ", r'^\d{4}-\d{2}-\d{2}$')
            new_time = validate_input("Enter a time for appointment (HH:MM): ", r'^\d{2}:\d{2}$')
            new_patient_id = validate_input("Enter patient ID: ", r'^P\d{3}$')
            new_patient_name = validate_input("Enter patient name: ", r'^[a-zA-Z\s]+$')
            new_sickness = validate_input("Enter the sickness you are having right now: ", r'^[a-zA-Z\s]+$')
            new_medicine = validate_input("Enter medicine: ", r'^[a-zA-Z\s]+$')
            new_total = float(input("Enter the total: RM"))
            new_next_appointment = validate_input("Do you want another appointment (Yes/No): ", r'^(yes|no)$')

            if new_next_appointment.lower() == "yes":
                new_appointment_date = validate_input("Enter date for the next appointment (YYYY-MM-DD): ", r'^\d{4}-\d{2}-\d{2}$')
            else:
                new_appointment_date = "N/A"  # Set to "N/A" if no further appointment
            
            new_remarks = input("Enter new remarks: ")

            # Convert row to a list for modification
            row_list = list(row)
            # Update row list with new values
            row_list[0] = new_date
            row_list[1] = new_time
            row_list[2] = new_patient_id
            row_list[3] = new_patient_name
            row_list[4] = new_sickness
            row_list[5] = new_medicine
            row_list[6] = new_total
            row_list[7] = new_next_appointment
            row_list[8] = new_appointment_date
            row_list[9] = new_remarks

            # Update the corresponding row in the worksheet
            for col_index, value in enumerate(row_list, start=1):
                ws2.cell(row=row_index, column=col_index, value=value)

            # Save the updated workbook
            wb.save(data_file)
            print()
            print("Patient details updated successfully.")
            print()
            return

        # Increment row index for the next iteration
        row_index += 1

    print("Patient ID not found. Please try again.")


