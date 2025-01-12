# shopping_list_manager.py

def display_menu():
    print(f"Shopping List Manager")
    print(f"1. Add Item")
    print(f"2. Remove Item")
    print(f"3. View List")
    print(f"4. Exit")

def add_item(shopping_list):
    item = input(f"Enter the item to add: ").strip()
    shopping_list.append(item)
    print(f"'{item}' has been added to the list.")

def remove_item(shopping_list):
    item = input(f"Enter the name of the item to remove: ").strip()
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"'{item}' has been removed from the list.")
    else:
        print(f"'{item}' was not found in the list.")

def view_list(shopping_list):
    if shopping_list:
        print(f"Current Shopping List:")
        for i, item in enumerate(shopping_list, start=1):
            print(f"{i}. {item}")
    else:
        print(f"The shopping list is currently empty.")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input(f"Choose an option (1-4): ").strip()
        
        if choice == "1":
            add_item(shopping_list)
        elif choice == "2":
            remove_item(shopping_list)
        elif choice == "3":
            view_list(shopping_list)
        elif choice == "4":
            print(f"Exiting Shopping List Manager. Goodbye!")
            break
        else:
            print(f"Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
