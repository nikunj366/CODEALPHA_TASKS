# 🤖 Basic Chatbot

## 📌 Project Description

This project is a simple rule-based chatbot developed using Python as part of the **CodeAlpha Python Programming Internship - Task 4**.

The chatbot interacts with users through predefined responses based on their input. It uses conditional statements, functions, loops, and basic input/output operations to simulate a conversation.

---

## 🚀 Features

* Responds to greetings
* Answers predefined questions
* Accepts both uppercase and lowercase input
* Handles extra spaces using `.strip()`
* Runs continuously until the user types `bye`
* User-friendly console interface

---

## 🛠 Technologies Used

* Python
* Functions
* If-Elif-Else Statements
* While Loops
* String Manipulation
* Input/Output Operations

---

## 📂 Project Structure

```text
CODEALPHA_BASIC_CHATBOT
│
├── main.py
└── README.md
```

---

## ⚙️ How It Works

### Step 1

The user enters a message.

### Step 2

The chatbot converts the input to lowercase and removes extra spaces.

```python
user_input = user_input.strip().lower()
```

### Step 3

The chatbot checks the input using `if-elif-else` statements.

### Step 4

A predefined response is returned.

### Step 5

The conversation continues until the user enters:

```text
bye
```

---

## ▶️ Run the Program

Open a terminal and run:

```bash
python main.py
```

---

## 💬 Supported Commands

| User Input        | Chatbot Response         |
| ----------------- | ------------------------ |
| hello             | Hi! 👋                   |
| how are you       | I'm fine, thanks! 😊     |
| what is your name | I am a Python Chatbot 🤖 |
| bye               | Goodbye! 👋              |

---

## 📸 Sample Output

```text
========================================
🤖 BASIC CHATBOT
Type 'bye' to exit
========================================

User: hello
Nova: Hi! 👋

User: how are you
Nova: I'm fine, thanks! 😊

User: what is your name
Nova: I am a Python Chatbot 🤖

User: bye
Nova: Goodbye! 👋
```

---

## 📚 Concepts Used

* Functions
* Conditional Statements
* While Loops
* String Methods
* User Input Handling
* Console Output

---

## 🎯 Learning Outcomes

Through this project, I learned:

* Creating functions in Python
* Using if-elif-else statements
* Handling user input
* Working with loops
* Building a simple conversational chatbot
* Improving user experience using string manipulation

---

## 👨‍💻 Author

**Nikunj Darji**

CodeAlpha Python Programming Internship Project
