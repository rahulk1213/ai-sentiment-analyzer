📌 BOTH PROJECTS AIp SENTIMENT ANALYZER & SECURITY AUTHENTICATION STYSTEM

# ai-sentiment-analyzer
🧠 AI Sentiment Analyzer — Python Project using TextBlob
The AI Sentiment Analyzer is a Python-based natural language processing (NLP) project designed to automatically detect and classify the sentiment of text data as positive, negative, or neutral. It leverages the TextBlob library for sentiment analysis, making it simple yet powerful for beginners and intermediate Python learners.

🚀 Key Features:
● Sentiment Detection: Analyzes input text and identifies the polarity (positive, negative, neutral).

● User Input Support: Accepts custom user input for real-time sentiment prediction.

■ Clean Output: Displays sentiment polarity score and a clear sentiment label.

¤ Lightweight & Efficient: Uses minimal dependencies, ideal for small-scale projects or learning purposes.

●Technologies Used:
Language: Python

Library: TextBlob (built on top of NLTK and Pattern)

📄 How It Works:
The user enters a sentence or paragraph.

The TextBlob library processes the text to compute:

Polarity: Ranges from -1 (negative) to +1 (positive)

Subjectivity: Degree of personal opinion

Based on the polarity value, the sentiment is classified as:

Positive (polarity > 0)

Negative (polarity < 0)

Neutral (polarity = 0)

Output is displayed with the polarity score and sentiment label.

📌 Sample Output:
Input: "I love this beautiful day!"
Polarity: 0.85
Sentiment: Positive



sentiment is classified as:

Positive (polarity > 0)

Negative (polarity < 0)

Neutral (polarity = 0)

Output is displayed with the polarity score and sentiment label.



🔐 Secure Authentication System — Python Project with getpass & hashlib
This project is a simple and secure user authentication system implemented in Python. It allows users to register and log in using a username and password, with password security handled using SHA-256 hashing from the hashlib library and password input protection using getpass.

💡 Features:
👤 User Registration with unique username check

🔐 Secure Login with hashed password verification

🧂 SHA-256 Password Hashing to prevent plain-text storage

🛡️ No Password Echoing using getpass for input privacy

💬 User-friendly CLI Interface for smooth interaction

🛠️ Technologies & Libraries:
Python (Core)

getpass — Securely handles password inputs

hashlib — Hashes passwords with SHA-256 algorithm

⚙️ How It Works:
Register:

User inputs a username and password (hidden via getpass)

Passwords are confirmed and hashed using SHA-256

The hashed password is stored in the users dictionary

Login:

User inputs their username and password

The entered password is hashed and matched with the stored hash

🔐 Secure Authentication System — Python Project using getpass & hashlib
📌 Project Overview:
This project is a console-based user authentication system developed in Python. It allows users to register and log in securely by using password hashing (via hashlib) and hidden password input (via getpass). It's ideal for learning how real-world authentication mechanisms work at a basic level.

🚀 Key Features:
👤 User Registration with password confirmation

🔐 Secure Login System with hashed password verification

🧂 SHA-256 Password Hashing to prevent plain-text storage

👁️‍🗨️ Hidden Password Input using getpass (for secure entry)

🖥️ Command-Line Interface (CLI) for smooth interaction

🛠️ Technologies Used:
Python (Core language)

getpass — Prevents passwords from being visible while typing

hashlib — Encrypts passwords using SHA-256 hashing

⚙️ How It Works:
Register:

The user enters a unique username.

Then enters and confirms the password (input is hidden).

The password is converted to a SHA-256 hash and stored in a dictionary.

Login:

The user enters their username and password.

The password entered is hashed and compared with the stored hash.

If the username exists and the hashes match, login is successful.

Exit:

User can exit the program at any time.

💻 Sample Console Output:
==== Secure Authentication System ====
1. Register
2. Login
3. Exit

Enter your choice: 1

--- Register New User ---
Enter a username: sanna
Enter password: ******
Confirm password: ******

✅ User registered successfully!
