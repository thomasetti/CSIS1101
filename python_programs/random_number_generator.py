import random

def generate_random_integers_file(filename, num_integers, min_value, max_value):
    with open(filename, 'w') as file:
        for _ in range(num_integers):
            file.write(f"{random.randint(min_value, max_value)}\n")

# Parameters
filename = "numberfile.txt"
num_integers = 100  # Number of random integers
min_value = 0       # Minimum value of random integers
max_value = 1000    # Maximum value of random integers

# Generate the file
generate_random_integers_file(filename, num_integers, min_value, max_value)
print(f"Generated {filename} with {num_integers} random integers.")