import random


def create_list(list_size):
    """ Create a list of random numbers """
    my_list = []

    for i in range(list_size):
        my_list.append(random.randrange(100))

    return my_list


def check_if_one_item_has_property_v1(my_list, key):
    """
    Return true if at least one item has a
    property.
    """
    list_position = 0
    while list_position < len(my_list) and my_list[list_position] != key:
        list_position += 1

    if list_position < len(my_list):
        # Found an item with the property
        return True
    else:
        # There is no item with the property
        return False


def check_if_one_item_has_property_v2(my_list, key):
    """
    Return true if at least one item has a
    property.
    """
    for item in my_list:
        if item == key:
            # Found an item that matched. Return True
            return True

    # Went through the whole list. Return False.
    return False


def check_if_all_items_have_property(my_list, key):
    """
    Return true if at ALL items have a property.
    """
    for item in my_list:
        if item != key:
            # Found an item that didn't match. Return False.
            return False

    # Got through the entire list. There were no mis-matches.
    return True


def get_matching_items(my_list, key):
    """
    Build a brand new list that holds all the items
    that match our property.
    """
    matching_list = []
    for item in my_list:
        if item == key:
            matching_list.append(item)
    return matching_list


def main():

    # Create a list of 50 numbers
    my_list = create_list(50)
    print(my_list)

    # Is at least one item zero?
    key = 0
    result = check_if_one_item_has_property_v1(my_list, 0)
    if result:
        print("At least one item in the list is", key)
    else:
        print("No item in the list is", key)

    # Get items that match the key
    matching_list = get_matching_items(my_list, key)
    print("Matching items:", matching_list)

    # Are all items matching?
    result = check_if_all_items_have_property(my_list, key)
    print("All items in random list matching?", result)

    other_list = [0, 0, 0, 0, 0]
    result = check_if_all_items_have_property(other_list, key)
    print("All items in other list matching?", result)


main()
