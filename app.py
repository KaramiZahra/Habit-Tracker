def load_habits():
    pass


def show_habits():
    pass


def add_habit():
    pass


def delete_habit():
    pass


def mark_habit():
    pass


def view_streaks():
    pass


def save_habits():
    pass


def menu():
    while True:
        print("\n---Habit Tracker---\n")
        print("1.Show all habits")
        print("2.Add a habit")
        print("3.Delete a habit")
        print("4.Mark habit as done")
        print("5.View streaks")
        print("6.Save and exit")

        option = input("Choose an option(1-6): ")
        if option == "1":
            show_habits()
        elif option == "2":
            add_habit()
        elif option == "3":
            delete_habit()
        elif option == "4":
            mark_habit()
        elif option == "5":
            view_streaks()
        elif option == "6":
            save_habits()
            break
        else:
            print("\nEnter a valid number.")


menu()
