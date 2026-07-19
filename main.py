import warnings
from openpyxl import load_workbook
import CreateData
import EditData
import DeleteData
import AddAppDateDetails
import PrintBill
import EditApp
import GenerateReport
import datetime
import time
import os


#Done by (Cheng Zheng De, 2207492) on 29/04/2024

#Clear screen before switching to other program
def clear_screen():

    if os.name=='posix':
        os.system('clear') #Clear screen for Mac And Linux

    else:
        os.system('cls')  #Clear screen for Windows

#Define column names for reading Excel data
column = ['Date', 'Time', 'Patient ID', 'Patient Name', 'Sickness', 'Medicine', 'Total', 'Next Appointment (Yes/No)', 'Appointment Date', 'Remarks']
        
#Allow the users to choose the Menu Options
def menu(wb, ws1, ws2, data_file):
    while True:
        print("     Welcome to UTAR Hospital Management System !!!") #Display welcome message

        #Get the current date and time
        today = datetime.datetime.today()
        a=today.strftime('%B %d %Y')
        d= today.strftime(" %H:%M:%S")

        #Display the current date and time
        print("-------------------------------------------------------")
        print("Current date:", a,'\tCurrent time:',d,'\n')
        print("-------------------------------------------------------")

        #Display the Menu Options
        print("\n===== Menu Options =====")
        print("<001>: Create new patient account")
        print("<002>: Edit patient account")
        print("<003>: Delete patient account")
        print("<004>: Add appointment date and treatment detail")
        print("<005>: Edit appointment date and treatment detail")
        print("<006>: Print bill for patient")
        print("<007>: Generate Report for each month")
        print("<008>: Exit System\n")

        #Get the Menu Options code input from the users
        menu_choose = input("Enter code: ")

        if menu_choose == "001": #Enter 001 to Create new patient account
            CreateData.AddPatient(ws1, wb, data_file)
            
        elif menu_choose == "002": #Enter 002 to Edit patient account
            EditData.EditPatient(ws1, wb, data_file)
            
        elif menu_choose == "003": #Enter 003 to Delete patient account
            DeleteData.DeletePatient(ws1, wb, data_file)
            
        elif menu_choose == "004": #Enter 004 to Add appointment date and treatment detail
            AddAppDateDetails.AddAppDateAndDetails(ws2, wb, data_file)
            
        elif menu_choose == "005": #Enter 005 to Edit appointment date and treatment detail
            EditApp.EditAppointment(ws2, wb, data_file)
            
        elif menu_choose == "006": #Enter 006 to Print bill for patient
            PrintBill.print_bill(wb, ws2)
            
        elif menu_choose == "007": #Enter 007 to Generate Report for each month
            GenerateReport.generate_report(data_file)
            
        elif menu_choose == "008": #Enter 008 to Exit System
            print()
            print("                    ╔════════════════════════════════════════════════════════════════════════╗")
            print("                    ║                             Take Care!                                 ║")
            print("                    ║                                                                        ║")
            print("        ╔═══════════╝                                                                        ╚═══════════╗")
            print("        ║                                                                                                ║")
            print("        ║            Exiting System. Thank you for using the UTAR Hospital Management System.            ║")                                                                                 
            print("        ║                                                                                                ║")
            print("        ╚═══════════╗                                                                        ╔═══════════╝")
            print("                    ║                                                                        ║")
            print("                    ║                             Stay Safe!                                 ║")
            print("                    ╚════════════════════════════════════════════════════════════════════════╝")

            print()
            print("The program will be closed in 5 seconds .....")
            time.sleep(5) #Will clear out the screen and exit the program in 5 seconds
                  
            wb.save(data_file)  #Save workbook before exiting
            break #Get out of the While loop to Exit the System
        
        else:
            print("Invalid code. Please try again.") #Input validation
            print()

#Main Program
def main():
    # Filter and ignore UserWarning from openpyxl module
    warnings.filterwarnings('ignore', category=UserWarning, module='openpyxl')

    # Specify the full path to the Excel file
    data_file = r'Hospital.xlsx'

    # Load the workbook and specify worksheets
    wb = load_workbook(data_file)
    ws1 = wb['MasterList']
    ws2 = wb['Treatment_Detail']

    # Call the menu function to start the program
    menu(wb, ws1, ws2, data_file)

if __name__ == "__main__":
    main()  # Call the main function to execute the program

clear_screen()#Clear the screen after the user exit the program
