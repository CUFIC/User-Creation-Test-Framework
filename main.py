#Functions
user_data = []
# Function to clear the terminal
def clear():
  print('\033c')

# Function to add a new user
def add_user(username, password):
    user_data.append({"username": username, "password": password})
    print(f"User '{username}' added successfully!")
    with open("users.txt", "a") as file:
        file.write(f"{username},{password}\n")

# Function to load user data from the file
def load_user_data():
    try:
        with open("users.txt", "r") as file:
            for line in file:
                username, password = line.strip().split(",")
                user_data.append({"username": username, "password": password})
    except FileNotFoundError:
        print("No user data found. Starting fresh.")
        print("")


# Load existing user data from the file
load_user_data()

#This is for different sign in and create account options
signinrange = ["signin", "sign in", "register", "login", "log in", "Signin", "Sign In", "Signin", "Login", "Log In"]
createrange = ["create", "create account", "new account", "new user", "signup", "register", "Sign Up", "Sign up", "Register", "Create Account", "New Account", "Create"]

#Starts the while loop
login = False
# Ask the user if they want to sign in or create an account
signin = input("Do you want to sign in or create an account? (signin/create): ")

while login == False:
    # prompt the user again
    if signin == None:
        clear()
        print("")
        signin = input("Do you want to sign in or create an account? (signin/create): ")

    if signin in createrange:
        print()
        # Prompt the user to create a new account
        usernamecreate= input("Please create a username: ")
        print()
        passwordcreate = input("Please create a strong password: ")
        # Call the add_user function to add the new user
        add_user(usernamecreate, passwordcreate)
        # Resets the "signin" variable to None to prompt again
        signin = None
        clear()


    if signin in signinrange:
        # Prompt the user to sign in
        clear()
        print("")
        usernameinput = input("Please enter your username: ")
        clear()
        # Read the user data from the file
        with open("users.txt", "r") as file:

            # If the user is in the saved data file, check the password
            if usernameinput in [username["username"] for username in user_data]:
                print("Username found!\n")
                passwordinput = input("Please enter your password: ")
                print()
                clear()
                # Check if the password matches the username
                if passwordinput == next(username["password"] for username in user_data if username["username"] == usernameinput):
                    print("Login successful! welcome " + usernameinput + ".")
                    # Set login to True to exit the loop and sign in
                    login = True
                # If the password does not match, print an error message and restart the loop
                else:
                    clear()
                    print("Incorrect password.\n")
                    signin = None
            # If the username is not found, print an error message and restart the loop
            else: 
                clear()
                print("Username not found. Please create an account first.\n")
                signin = None
    # If the input is not recognized, prompt the user again
    if signin not in createrange and signin not in signinrange and signin is not None:
        clear()
        print()
        print("Invalid input. Please enter 'signin' or 'create'.\n")
        signin = None