def welcome():
    """
    Display a welcome message.
    """
    pass


def check_item_in_list(item, shopping_list):
    """
    Return True if item is in the list, otherwise false
    """
    pass

def add_item(item, shopping_list):
    """
    Add item to shopping list if it doesn't exist
    """
    pass


def add_items(shopping_list)-> [str]:
    """
    get items from user using get_user_input function.
    add all items until input is "done"
    """
    pass

def get_user_input():
    """
    display message to user telling how to write input,
    return user input
    """
    user_input = input("Add an item (type 'done' to finish): ").strip()
    return user_input

def show_list(shopping_list):
    """
    Display the current shopping list.
    """
    

def remove_item(item, shopping_list):
    """
    remove item from shopping list if exists in it
    """



# 6. Main API flow
def main():
    welcome()
    shopping_list = []
    check_item_in_list("milk", shopping_list)
    add_items(shopping_list=shopping_list)
    show_list(shopping_list=shopping_list)

    # Example check and remove
    check_item_in_list("milk", shopping_list=shopping_list)
    remove_item("milk", shopping_list=shopping_list)
    show_list(shopping_list=shopping_list)


# Run the API if file is executed directly
if __name__ == "__main__":
    main()
