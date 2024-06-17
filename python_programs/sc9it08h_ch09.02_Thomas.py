def write_message(message, length):
    # Helper function to write out the message sc9it08h_ch09.02 part b
    print("Message: ", end="")
    for i in range(length):
        print(message[i], end="")
    print()

def encode_message(message, length, shift):
    # Function to encode the message using Caesar cipher sc9it08h_ch09.02 part c
    for i in range(length):
        if 'A' <= message[i] <= 'Z':
            new_char = chr((ord(message[i]) - ord('A') + shift) % 26 + ord('A'))
            message[i] = new_char

def decode_message(message, length, shift):
    # Function to decode the message back to original form sc9it08h_ch09.02 part d
    for i in range(length):
        if 'A' <= message[i] <= 'Z':
            new_char = chr((ord(message[i]) - ord('A') - shift) % 26 + ord('A'))
            message[i] = new_char

def main():
    # Collect the message from the user sc9it08h_ch09.02 part a
    message = []
    print("Enter up to 10 CAPITAL letters for the message, one per line. Enter '%' to terminate input.")
    while len(message) < 10:
        char = input(f"Character {len(message) + 1}: ").strip().upper()
        if char == '%':
            break
        if len(char) == 1 and 'A' <= char <= 'Z':
            message.append(char)
        else:
            print("Invalid input. Please enter a single uppercase letter.")

    length = len(message)
    if length == 0:
        print("No message entered.")
        return

    write_message(message, length)
    
    # Ask for the shift amount
    while True:
        try:
            shift = int(input("Enter the shift amount (0-25): "))
            if 0 <= shift <= 25:
                break
            else:
                print("Please enter a value between 0 and 25.")
        except ValueError:
            print("Invalid input. Please enter an integer between 0 and 25.")

    # Encode the message
    encode_message(message, length, shift)
    write_message(message, length)

    # Decode the message back to original
    decode_message(message, length, shift)
    write_message(message, length)

if __name__ == "__main__":
    main()