# 📧 Email Extractor & Report Generator

## 📌 Project Description

Email Extractor & Report Generator is a Python automation project developed as part of the **CodeAlpha Python Programming Internship (Task 3)**.

This application scans all supported files inside a user-specified folder, extracts email addresses using Regular Expressions (Regex), removes duplicate emails, generates domain statistics, and exports the results into an Excel report.

---

## 🚀 Features

* Scan an entire folder automatically
* Extract email addresses using Regex
* Support multiple file formats:

  * `.txt`
  * `.csv`
  * `.log`
  * `.md`
  * `.py`
* Remove duplicate email addresses
* Sort extracted emails alphabetically
* Generate domain-wise statistics
* Export results to Excel format (`.xlsx`)
* Create timestamp-based reports
* Automatically save reports inside the **Reports** folder

---

## 📂 Project Structure

```text
CODEALPHA_Task Automation with Python Scripts
│
├── Reports
│   └── Email_Report_DD-MM-YYYY_HH-MM-SS.xlsx
│
├── sample
│   └── emails.txt
│
├── main.py
└── README.md
```

---

## 🛠 Technologies Used

* Python
* Regular Expressions (`re`)
* File Handling
* OS Module (`os`)
* Collections (`Counter`)
* Date & Time (`datetime`)
* OpenPyXL

---

## ⚙️ How It Works

### Step 1

User enters the folder path to scan.

### Step 2

The program scans all supported files in the folder.

### Step 3

Email addresses are extracted using the following Regex pattern:

```python
email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
```

### Step 4

Duplicate emails are removed using Python Sets.

### Step 5

Domains are extracted from email addresses.

Example:

```text
support@gmail.com
hr@yahoo.com
admin@gmail.com
```

Extracted Domains:

```text
gmail.com
yahoo.com
gmail.com
```

### Step 6

Domain statistics are calculated using `Counter()`.

### Step 7

An Excel report is generated containing:

#### Sheet 1: Extracted Emails

| Sr No | Email Address                                 |
| ----- | --------------------------------------------- |
| 1     | [admin@gmail.com](mailto:admin@gmail.com)     |
| 2     | [support@yahoo.com](mailto:support@yahoo.com) |
| 3     | [hr@company.org](mailto:hr@company.org)       |

#### Sheet 2: Statistics

| Domain      | Count |
| ----------- | ----- |
| gmail.com   | 4     |
| yahoo.com   | 2     |
| company.org | 1     |

---

## ▶️ Installation

Install the required package:

```bash
pip install openpyxl
```

---

## ▶️ Run the Program

```bash
python main.py
```

---

## 📊 Sample Output

```text
Scanning files...

Scanned: emails.txt
Emails Found: 7

===================================
EMAIL EXTRACTION COMPLETED
===================================

Total Emails Found     : 7
Unique Emails Found    : 7
Unique Domains Found   : 3

gmail.com : 3
yahoo.com : 2
outlook.com : 2

Report saved successfully!
```

---

## 📚 Python Concepts Used

* File Handling
* Loops
* Lists
* Sets
* String Manipulation
* Regular Expressions (Regex)
* Error Handling
* Counter Collections
* Excel File Generation
* Directory Operations

---

## 🎯 Learning Outcomes

Through this project, I learned:

* Working with files and folders
* Extracting data using Regex
* Removing duplicate records
* Creating Excel reports using OpenPyXL
* Automating repetitive tasks with Python
* Generating useful statistics from extracted data

---

## 👨‍💻 Author

**Nikunj Darji**

CodeAlpha Python Programming Internship Project
