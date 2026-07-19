from openpyxl import load_workbook
import pandas as pd

#Done by (Chew Yan Yu, 2206970) on 29/04/2024

def generate_report(data_file):
    try:
        # Load the workbook and select the appropriate worksheet
        wb = load_workbook(data_file)
        ws2 = wb['Treatment_Detail']

        # Set display options for Pandas DataFrame
        pd.set_option('display.max_columns', None)  # Display all columns
        pd.set_option('display.expand_frame_repr', False)  # Display without truncating columns

        # Read data from the Excel file, specifying the header row
        df = pd.read_excel(data_file, sheet_name='Treatment_Detail', header=2)

        # Check if the 'Date' column is not datetime64 type and convert it
        if not pd.api.types.is_datetime64_any_dtype(df['Date']):
            df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

        # Display content from the Excel file
        print("===== Content from Excel File =====\n")
        print(df)
        print("\n===================================\n")

        # Ask the user for the month to generate the report for
        month_input = input("Enter month (1-12): ")

        # Convert the input to integer
        month = int(month_input)

        # Filter the DataFrame based on the month
        df_month = df[df['Date'].dt.month == month]

        if not df_month.empty:
            # Display the content for the specified month
            print(f"===== Content for Month {month} =====\n")
            print(df_month)
            print(f"\n===================================\n")

            # Ask the user if they want to generate a report
            user_choice = input(
                "Do you want to generate a report for this month? (Type 'y' for Yes, or press Enter to skip): ").strip().lower()
            if user_choice == 'y':
                report_filename = f'Report_Month_{month}.txt'
                df_month.to_csv(report_filename, index=False)
                print(f"Report saved as '{report_filename}'")
                print()
            else:
                print("Report generation skipped.")
                print()
        else:
            print(f"No data found for Month {month}.")
            print()

    except FileNotFoundError:
        print(f"Excel file '{data_file}' not found.")
        print()
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        print()

# Example usage:
# data_file = r'C:\Users\jason\Dropbox\PC\Downloads\Hospital.xlsx'
# generate_report(data_file)
