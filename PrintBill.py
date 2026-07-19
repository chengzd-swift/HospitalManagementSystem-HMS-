def print_bill(wb, ws2):

    # Done by (Chew Yan Yu, 2206970) on 29/04/2024
    
    # Prompt user for patient ID
    patient_id = input("Enter Patient ID to print bill: ")

    found = False
    total_charges = 0  # Initialize total_charges with 0

    for row in ws2.iter_rows(values_only=True):
        if row[2] == patient_id:
            found = True

            # Extract relevant information from the row
            date = row[0]
            time = row[1]
            name = row[3]

            # Accumulate total charges
            total_charges += float(row[6])  # Accumulate total charges

            # Print patient details for the first matching row
            if found:
                print()
                print("Patient Details: \n")
                print("Patient ID:", patient_id)
                print("Patient Name:", name)
                print("Date:", date)
                print("Time:", time)
                print()

    if found:
        # Print the accumulated total charges for all matching rows
        print("Total Charges: RM", total_charges)
        print()
    else:
        print("Patient ID not found.")
        print()

    # Write patient details and total charges to text file
    with open('Patient_Bill.txt', 'w') as f:
        if found:
            f.write("Patient Details:\n")
            f.write("Patient ID: {}\n".format(patient_id))
            f.write("Patient Name: {}\n".format(name))
            f.write("Total Charges: RM{}\n".format(total_charges))
        else:
            f.write("Patient ID not found.\n")
