from getpass import getpass
from hashlib import sha256

users = {}

def register():
    print("\n--- Register New User ---")
    username = input("Enter a username: ")

    if username in users:
        print(" Username already exists. Try a different one.")
        return

    password = getpass("Enter password: ")
    confirm = getpass("Confirm password: ")

    if password != confirm:
        print(" Passwords do not match!")
        return

    hashed_password = sha256(password.encode()).hexdigest()
    users[username] = hashed_password
    print(" User registered successfully!")

def login():
    print("\n--- User Login ---")
    username = input("Enter your username: ")
    password = getpass("Enter your password: ")

    hashed_password = sha256(password.encode()).hexdigest()

    if username in users and users[username] == hashed_password:
        print(f"✅ Login successful! Welcome, {username} ")
    else:
        print("❌ Invalid username or password.")

def main():
    while True:
        print("\n==== Secure Authentication System ====")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            register()
        elif choice == '2':
            login()
        elif choice == '3':
            print(" Exiting the program.")
            break
        else:
            print("❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
