# Prompt the user to input the PIN to be hacked
pin = input("Assign a 6 numeric-character PIN: ")

# Define the characters that can be used in the PIN (digits 0-9)
possible_characters = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")

# Initialize list to hold the current attempt at the PIN
tries = ["", "", "", "", "", ""]  # Increased to match the length of the PIN being guessed

# Variable to store the current password attempt
test_password = ""

if len(pin) == 6:
    # Inform the user that the hacking process is starting
    print("Starting the hack...")
    # Loop until the correct PIN is found
    while test_password != pin:
        # Nested loops to iterate through all possible combinations of PIN digits
        for a in possible_characters:
            tries[0] = a  # First position in the PIN attempt
            for b in possible_characters:
                tries[1] = b  # Second position in the PIN attempt
                for c in possible_characters:
                    tries[2] = c  # Third position in the PIN attempt
                    for d in possible_characters:
                        tries[3] = d  # Fourth position in the PIN attempt
                        for e in possible_characters:
                            tries[4] = e  # Fifth position in the PIN attempt
                            for f in possible_characters:
                                tries[5] = f  # Sixth position in the PIN attempt

                                # Construct the current attempt at the PIN
                                test_password = tries[0] + tries[1] + tries[2] + tries[3] + tries[4] + tries[5]
                                # Print the current PIN attempt for user feedback
                                print(test_password)

                                # Check if the current attempt matches the PIN
                                if test_password == pin:
                                    break  # Exit the innermost loop if the PIN is found

                            if test_password == pin:
                                break  # Exit the fifth position loop if the PIN is found

                        if test_password == pin:
                            break  # Exit the fourth position loop if the PIN is found

                    if test_password == pin:
                        break  # Exit the third position loop if the PIN is found

                if test_password == pin:
                    break  # Exit the second position loop if the PIN is found

            if test_password == pin:
                break  # Exit the first position loop if the PIN is found

    # Print the PIN once it has been successfully hacked
    print("The PIN is " + test_password)

else:
    print("Invalid PIN length, please enter a 6 digit PIN...")
