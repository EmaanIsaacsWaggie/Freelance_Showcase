# Reading input string from the user
input_string = input("Enter a string ")

# Initialize an empty string to store the modified string
modified_string = ""

# Iterate over each character in the input string for i in range(len(input_string)):
# Check if index is even or odd
for i in range(len(input_string)):
    if i % 2 == 0:
        # Convert the character to a lowercase and add to the modified string
        modified_string += input_string[i].lower()
    else:
        modified_string += input_string[i].upper()
print("modified string:" , modified_string)

# Reading input string from the user
input_string = input("Enter a string ").split()

# Part 2 of task.

for i in range(len(input_string)):
    if i % 2 == 0:
        #
         input_string[i] = input_string[i].lower()
    else:
        input_string[i] = input_string[i].upper()
print(" ".join(input_string))
