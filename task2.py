import random

# Ask user for password
password = input("Enter your password: ")

# Check password length
if len(password) < 9:
    print("Password too short.")
    exit()

# Ask for 3 random character positions
for _ in range(3):
    position = random.randint(1, len(password))
    guess = input(f"Enter letter at position {position}: ")

    # Check if the entered letter is correct
    if guess == password[position - 1]:
        print("Correct")
    else:
        print("\nSecurity check failed.")
        exit()

# If all checks pass
print("\nSecurity check passed.")
