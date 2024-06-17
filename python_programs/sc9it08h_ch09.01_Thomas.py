def sequential_search(data, target):
    n = len(data)
    found = False
    index = 0

    while not found and index < n:
        if data[index] == target:
            found = True
        else:
            index += 1

    return found

def main():
    # Get the list of numbers seperated by spaces from the user
    data_input = input("Enter a list of integers separated by spaces: ")
    data = list(map(int, data_input.split()))

    # Get the number to be searched for in the list
    target = int(input("Enter the integer to search for: "))

    # Perform the sequential search
    if sequential_search(data, target):
        print("Successful search, this value is in the list.")
    else:
        print("Unsuccessful search, the value is not in the list.")

if __name__ == "__main__":
    main()
