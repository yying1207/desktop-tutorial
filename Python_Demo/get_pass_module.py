import getpass

# Avoid the password being displayed on the console when the user types it in, enhancing security by preventing shoulder surfing and unauthorized access to sensitive information.
print("Please enter your password:")
my_pass = getpass.getpass() # getpass() prompts the user for a password without echoing it to the console, providing a secure way to handle sensitive input.
my_pass = getpass.getpass(prompt="Enter your password: ") # You can also provide a custom prompt message to guide the user when asking for the password.

print("Entered password is:", my_pass)


# This will show the password as the user types it, which is not recommended for sensitive information.
password = input("Enter your password: ")


