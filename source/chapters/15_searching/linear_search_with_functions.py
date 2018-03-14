def read_in_file(file_name):
    """ Read in lines from a file """

    # Open the file for reading, and store a pointer to it in the new
    # variable "file"
    my_file = open(file_name)

    # Create an empty list to store our names
    name_list = []

    # Loop through each line in the file like a list
    for line in my_file:
        # Remove any line feed, carriage returns or spaces at the end of the line
        line = line.strip()

        # Add the name to the list
        name_list.append(line)

    my_file.close()

    return name_list


def linear_search(key, name_list):
    """ Linear search """

    # Start at the beginning of the list
    current_list_position = 0

    # Loop until you reach the end of the list, or the value at the
    # current position is equal to the key
    while current_list_position < len(name_list) and name_list[current_list_position] != key:

        # Advance to the next item in the list
        current_list_position += 1

    return current_list_position


def main():

    key = "Morgiana the Shrew"
    name_list = read_in_file("super_villains.txt")
    list_position = linear_search(key, name_list)

    if list_position < len(name_list):
        print("The name", key, "is at position", list_position)
    else:
        print("The name", key, "was not in the list.")


main()
