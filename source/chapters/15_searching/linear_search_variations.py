class AdventureObject:
    """ Class that defines an alien"""

    def __init__(self, description, room):
        """ Constructor. Set name and color"""
        self.description = description
        self.room = room


def has_property(my_object, room):
    """
    Check to see if an item has a property.
    In this case, is the object in the specified room?
    """
    if my_object.room == room:
        return True
    else:
        return False


def check_if_one_item_has_property_v1(my_list, room):
    """
    Return true if at least one item has a
    property.
    """
    i = 0
    while i < len(my_list) and not has_property(my_list[i], room):
        i += 1

    if i < len(my_list):
        # Found an item with the property
        return True
    else:
        # There is no item with the property
        return False


def check_if_one_item_has_property_v2(my_list, room):
    """
    Return true if at least one item has a
    property. Works the same as v1, but less code.
    """
    for item in my_list:
        if has_property(item, room):
            return True
    return False


def check_if_all_items_have_property(my_list, room):
    """
    Return true if at ALL items have a property.
    """
    for item in my_list:
        if not has_property(item, room):
            return False
    return True


def get_matching_items(my_list, room):
    """
    Build a brand new list that holds all the items
    that match our property.
    """
    matching_list = []
    for item in my_list:
        if has_property(item, room):
            matching_list.append(item)
    return matching_list


def main():
    object_list = []
    object_list.append(AdventureObject("Key", 5))
    object_list.append(AdventureObject("Bear", 5))
    object_list.append(AdventureObject("Food", 8))
    object_list.append(AdventureObject("Sword", 2))
    object_list.append(AdventureObject("Wand", 10))

    result = check_if_one_item_has_property_v1(object_list, 5)
    print("Result of test check_if_one_item_has_property_v1:", result)

    result = check_if_one_item_has_property_v2(object_list, 5)
    print("Result of test check_if_one_item_has_property_v2:", result)

    result = check_if_all_items_have_property(object_list, 5)
    print("Result of test check_if_all_items_have_property:", result)

    result = get_matching_items(object_list, 5)
    print("Number of items returned from test get_matching_items:", len(result))


main()