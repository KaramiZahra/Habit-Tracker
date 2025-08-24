import uuid
from datetime import datetime
import json
from pathlib import Path
from rich.table import Table
from rich.console import Console


HABITS_FILE = Path("habits.json")
habits = []
console = Console()


def load_habits():
    habits.clear()

    if HABITS_FILE.exists():
        try:
            with open(HABITS_FILE, 'r') as hf:
                habits.extend(json.load(hf))
        except json.JSONDecodeError:
            console.print(
                "[bold yellow]Warning: JSON file is corrupted. Starting with empty habits.[/bold yellow]")
    else:
        HABITS_FILE.touch()


load_habits()


def show_habits():
    if not habits:
        console.print("\n[bold red]No habits found.[/bold red]")
        return

    table = Table(
        title="\n[bold white]Habit Tracker[/bold white]", show_lines=True)

    table.add_column("ID", no_wrap=True)
    table.add_column("Name")
    table.add_column("Category")
    table.add_column("Frequency")
    table.add_column("Created At")

    colors = ["cyan", "magenta", "yellow", "green", "blue", "red", "white"]
    for i, h in enumerate(habits):
        row_color = colors[i % len(colors)]
        table.add_row(
            h['id'][:6],
            h['name'],
            h['category'],
            h['frequency'],
            h['created_at'],
            style=row_color
        )

    console.print(table)


def add_habit():
    habit_name = input("Enter habit name: ").strip().capitalize()
    habit_category = input("Enter habit category: ").strip().capitalize()

    frequency_map = {'1': 'Daily', '2': 'Weekly', '3': 'Monthly'}
    while True:
        frequency_option = input(
            "Choose habit frequency 1)Daily 2)Weekly 3)Monthly: ").strip()
        if frequency_option in frequency_map:
            habit_frequency = frequency_map[frequency_option]
            break
        console.print("[bold red]Invalid frequency.[/bold red]")

    new_habit = {
        'id': str(uuid.uuid4()),
        'name': habit_name,
        'category': habit_category,
        'frequency': habit_frequency,
        'created_at': datetime.now().date().isoformat()
    }

    habits.append(new_habit)
    console.print("\n[bold green]Habit successfully added.[/bold green]")


def delete_habit():
    pass


def mark_habit():
    pass


def view_streaks():
    pass


def save_habits():
    with open(HABITS_FILE, 'w') as hf:
        json.dump(habits, hf, indent=4)


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
            console.print("\n[bold red]Enter a valid number.[/bold red]")


menu()
