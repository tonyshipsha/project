import time

password_length = 6

start_time = time.time()
while True:
    pin = input(f"Assign a {password_length} numeric-character PIN: ")
    if pin.isdigit() and len(pin) == password_length:
        break
    else:
        print("Invalid input. Please enter a {password_length}-digit numerical PIN.")

# At this point, pin is guaranteed to be a 6-digit numerical PIN
print("PIN entered:", pin)


def generate_combinations(length):
    digits = "0123456789"
    if length == 0:
        yield ""  # Yield an empty string when length is 0
    else:
        for digit in digits:
            for sub_combination in generate_combinations(length - 1):
                yield digit + sub_combination


for combination in generate_combinations(password_length):
    print(combination)
    if combination == pin:
        print("The PIN is " + combination)
        break  # Exit the first position loop if the PIN is found

end_time = time.time()
elapsed_time = end_time - start_time
# Output the elapsed time
print(f"Elapsed time: {elapsed_time} seconds")
