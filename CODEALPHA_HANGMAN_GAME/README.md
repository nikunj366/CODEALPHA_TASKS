# 🎮 Hangman Game

## 📌 Project Description

Hangman Game is a simple text-based word guessing game developed using Python as part of the **CodeAlpha Python Programming Internship - Task 1**.

In this game, the computer randomly selects a word from a predefined list, and the player has to guess the word one letter at a time. The player is allowed a maximum of 6 incorrect guesses before the game ends.

---

## 🚀 Features

* Random word selection using Python's `random` module
* User guesses one letter at a time
* Maximum of 6 incorrect attempts allowed
* Input validation for incorrect inputs
* Prevents repeated guesses
* Displays progress after each guess
* Win and Lose conditions

---

## 🛠 Technologies Used

* Python
* Random Module
* Lists
* Strings
* Loops
* Conditional Statements
* User Input Handling

---

## 📂 Project Structure

```text
CODEALPHA_HANGMAN_GAME
│
├── main.py
└── README.md
```

---

## ⚙️ How the Game Works

### Step 1

The program selects a random word from a predefined list.

```python
words = ["apple", "mango", "penguin", "grapes", "horse"]
word = random.choice(words)
```

### Step 2

The selected word is hidden using underscores.

Example:

```text
_ _ _ _ _
```

### Step 3

The user enters a letter.

```text
Enter a letter: a
```

### Step 4

If the letter exists in the word, it is revealed.

```text
a _ _ _ _
```

### Step 5

If the letter does not exist, one attempt is deducted.

```text
Wrong Guess! Attempts left: 5
```

### Step 6

The game continues until:

* The player guesses the complete word (Win)
* Attempts become 0 (Lose)

---

## ▶️ Run the Program

Open a terminal and run:

```bash
python main.py
```

---

## 🎮 Sample Gameplay

```text
--------------------------
 Welcome to Hangman Game
--------------------------

Guess the word:
_ _ _ _ _

Enter a letter: a

Correct Guess!

a _ _ _ _

Enter a letter: z

Wrong Guess!
Attempts left: 5

Enter a letter: p

Correct Guess!

a p p _ _

Congratulations!
You guessed the word: apple
```

---

## 📚 Concepts Used

* Random Word Selection
* Lists
* String Manipulation
* While Loops
* If-Else Statements
* Input Validation
* User Interaction
* Game Logic

---

## 🎯 Learning Outcomes

Through this project, I learned:

* Using Python's random module
* Working with lists and strings
* Implementing loops and conditions
* Handling user input
* Creating a simple console-based game
* Managing game states and logic

---

## 🔮 Future Improvements

Possible enhancements:

* Difficulty Levels (Easy, Medium, Hard)
* Hint System
* Score Tracking
* ASCII Hangman Drawing
* Multiple Rounds
* GUI Version using Tkinter

---

## 👨‍💻 Author

**Nikunj Darji**

CodeAlpha Python Programming Internship Project
