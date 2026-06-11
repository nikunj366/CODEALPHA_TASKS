import os #use for file handling and Directory operations
import re #use for regular expression operations
from collections import Counter #use for counting hashable objects, in this case we will use it to count the frequency of email domains
from datetime import datetime #use for handling date and time, we will use it to create a timestamp for the report name
from openpyxl import Workbook #use for creating and manipulating Excel files, we will use it to create an Excel report of the extracted emails and their statistics

email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}' # re matech this email patter to extract email address from folder or files

folder_path = input("Enter folder path: ") # taking folder path from user as input 


supported_extensions = ('.txt', '.csv', '.log', '.md', '.py') # supppored file extentions


all_emails = [] # store extracted email address from all files in this list

print("\nScanning files...\n")

for file_name in os.listdir(folder_path): # search files in the give folder path

    if file_name.endswith(supported_extensions): # check is the file supported or not 

        file_path = os.path.join(folder_path, file_name) # creating full path with folder name and file name ex. C/Users/Username/Documents/file.txt

        try: # Exception handling to catch any error while reading the file
            with open(file_path, "r", encoding="utf-8") as file: # close the file after reading it 

                content = file.read() # read file and save it in content variable

                emails_found = re.findall(email_pattern, content) # use re.findall to find all the email address in the content of the file and save it in emails_found list

                all_emails.extend(emails_found) # store all the email address in all_emails list

                print(f"Scanned: {file_name}")
                print(f"Emails Found: {len(emails_found)}\n")

        except Exception as e: # if any file can't be read give us an msg without stopping the program
            print(f"Could not read {file_name}")
            print(e)

unique_emails = sorted(list(set(all_emails)))# use set to get unique email,make it list and sort it in alphabetical order

domains = [] # empty list to store email domin names.

for email in unique_emails: 
    domain = email.split("@")[1] # split email id into two parts using "@" as separator and take the second part which is the domain name and store it in domain variable, 1 is used to get the second part of the split result which is the domain name.
    domains.append(domain)

domain_counter = Counter(domains) # count the total number domain 


workbook = Workbook() # crete a new excel file
sheet1 = workbook.active
sheet1.title = "Extracted Emails"
sheet1["A1"] = "Sr No"
sheet1["B1"] = "Email Address"
for index, email in enumerate(unique_emails, start=1):

    sheet1.cell(row=index + 1, column=1, value=index)
    sheet1.cell(row=index + 1, column=2, value=email)

sheet2 = workbook.create_sheet("Statistics")
sheet2["A1"] = "Domain"
sheet2["B1"] = "Count"

row = 2

for domain, count in domain_counter.items():

    sheet2.cell(row=row, column=1, value=domain)
    sheet2.cell(row=row, column=2, value=count)

    row += 1

sheet2["D1"] = "Summary"
sheet2["D2"] = "Total Emails"
sheet2["E2"] = len(unique_emails)

sheet2["D3"] = "Unique Domains"
sheet2["E3"] = len(domain_counter)

timestamp = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")

report_name = f"Email_Report_{timestamp}.xlsx"

reports_folder = os.path.join(folder_path, "Reports")

os.makedirs(reports_folder, exist_ok=True)

report_path = os.path.join(reports_folder, report_name)

workbook.save(report_path)

print(f"Report saved at:\n{report_path}")
print("\n===================================")
print("EMAIL EXTRACTION COMPLETED")
print("===================================")

print(f"Total Emails Found     : {len(all_emails)}")
print(f"Unique Emails Found    : {len(unique_emails)}")
print(f"Unique Domains Found   : {len(domain_counter)}")

print("\nDomain Statistics:")

for domain, count in domain_counter.items():
    print(f"{domain} : {count}")

print(f"\nExcel Report Saved As:")
print(report_name)

print("\nDone Successfully!")