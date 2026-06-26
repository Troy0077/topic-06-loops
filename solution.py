# Topic 06 Collaborative Assignment
# Your Name: Troy Post
# Date: 6/26/2026

# --- STARTER CODE ---
# This function takes a number and returns its square.
def square(n):
    return n * n

# This loop calls the function for numbers 1 through 5.
for i in range(1, 6):
    result = square(i)
    print(i, "squared is", result)

# --- YOUR EXTENSION BELOW THIS LINE ---
# Ideas: Write a second function, change the range,
# change what the function does, or add a while loop
# that lets the user keep entering numbers until they type "quit".
def cube(n):
  retuurn n * n * n 

print("\n--- Starting Interactive Mode ---")

while True:
    user_input = input("Enter a number to cube (or type 'quit' to exit): ")
    
    if user_input.lower() == 'quit':
        print("Thanks for playing! Goodbye.")
        break

  if user_input.isdigit():
        number = int(user_input)
        cube_result = cube(number)
        print(f"{number} cubed is {cube_result}\n")
    else:
        print("Please enter a valid number or 'quit'.\n")
