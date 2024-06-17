def sequential_search(data, target):
    n = len(data)
    found = False
    index = 0

    while not found and index < n:
        if data[index] == target:
            found = True
        else:
            index += 1

    return index if found else -1

def read_integers_from_file(filename):
    with open(filename, 'r') as file:
        return [int(line.strip()) for line in file]

def main():
    # Read the list of numbers from the file
    filename = "numberfile.txt"
    data = read_integers_from_file(filename)

    # Get the number to be searched for in the list
    target = int(input("Enter the integer to search for: "))

    # Perform the sequential search
    index = sequential_search(data, target)
    
    if index != -1:
        print(f"Successful search, this value is in the list at index {index}.")
    else:
        print("Unsuccessful search, the value is not in the list.")

if __name__ == "__main__":
    main()