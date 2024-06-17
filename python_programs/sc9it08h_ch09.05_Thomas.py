def read_integers_from_file(filename):
    with open(filename, 'r') as file:
        return [int(line.strip()) for line in file]

def write_integers_to_file(filename, data):
    with open(filename, 'w') as file:
        for item in data:
            file.write(f"{item}\n")

def find_largest_location(data, end):
    # Find the location of the largest number in the unsorted section
    largest_index = 0
    for i in range(1, end + 1):
        if data[i] > data[largest_index]:
            largest_index = i
    return largest_index

def selection_sort(data):
    n = len(data)
    for end in range(n - 1, 0, -1):
        largest_index = find_largest_location(data, end)
        # Swap the largest number with the last number in the unsorted section
        data[largest_index], data[end] = data[end], data[largest_index]

def main():
    # Read the list of numbers from the file
    input_filename = "numberfile.txt"
    output_filename = "sortednumbers.txt"
    data = read_integers_from_file(input_filename)

    # Perform the selection sort
    selection_sort(data)

    # Write the sorted list to another file
    write_integers_to_file(output_filename, data)
    print(f"Sorted data has been written to {output_filename}")

if __name__ == "__main__":
    main()