# This is a basic Python script

# Function to greet the user
def greet_user(name):
    print(f"Hello, {name}! Welcome to the Python script.")

# Main function
def main():
    user_name = input("Enter your name: ")  # Ask for user input
    greet_user(user_name)  # Call greet_user function with the input name

# Check if the script is being run directly (not imported as a module)
if __name__ == "__main__":
    main()
