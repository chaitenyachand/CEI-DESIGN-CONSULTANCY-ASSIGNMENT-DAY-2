# Create a program that takes user input to add multiple elements to an array, then prints the final array

def main():
    # Initialize an empty array
    array = []

    # Loop to take user input
    while True:
        # Ask for user input
        element = input("Enter an element to add to the array (or type 'done' to finish): ")

        # Check if the user wants to stop
        if element.lower() == 'done':
            break

        # Add the element to the array
        array.append(element)

    # Print the final array
    print("The final array is:", array)

if __name__ == "__main__":
    main()
