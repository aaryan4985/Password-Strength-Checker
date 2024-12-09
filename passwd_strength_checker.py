import re

# Function to check the password's strength
def check_password_strength(password):
    strength = 0
    feedback = []
    
    # 1. Password length (minimum 8 characters)
    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters long.")
    
    # 2. Uppercase and lowercase letters
    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        strength += 1
    else:
        feedback.append("Include both uppercase and lowercase letters.")
    
    # 3. Numbers
    if re.search(r'\d', password):
        strength += 1
    else:
        feedback.append("Include at least one number.")
    
    # 4. Special characters
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        strength += 1
    else:
        feedback.append("Include at least one special character (!, @, #, etc.).")
    
    # Overall feedback
    if strength == 4:
        feedback = ["Your password is strong!"]
    elif strength >= 2:
        feedback.insert(0, "Your password is medium.")
    else:
        feedback.insert(0, "Your password is weak.")
    
    return strength, feedback

# Main function to run the password strength checker
def main():
    print("\n--- Password Strength Checker ---")
    print("\n*** What makes a strong password? ***")
    print("- At least 8 characters long.")
    print("- Includes both uppercase and lowercase letters.")
    print("- Contains at least one number.")
    print("- Has at least one special character (e.g., !, @, #, etc.).\n")
    
    choice = "y"  # Initialize choice variable for the first iteration
    while choice.lower() == "y":
        password = input("Enter your password: ")
        strength, feedback = check_password_strength(password)
        
        # Display the strength score and feedback
        print(f"\nPassword Strength: {strength}/4")
        print("Feedback:")
        for f in feedback:
            print(f"- {f}")
        
        # Ask the user if they want to check another password
        choice = input("\nDo you want to check another password? (y/n): ")

if __name__ == "__main__":
    main()
