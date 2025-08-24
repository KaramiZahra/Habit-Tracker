# Habit Tracker (CLI)

A simple command-line interface (CLI) habit tracker written in Python. Track your daily habits and view your streaks over time.

## Features

- Add and delete habits
- Track daily completions of habits
- View streaks for each habit
- Save and load habits from a JSON file

## Installation

1. Clone the repository:

```bash
git clone https://github.com/KaramiZahra/Habit-Tracker
cd Habit-Tracker
```

2. Make sure you have Python 3 installed.

3. Install required dependencies:

```bash
pip install rich
```

## Usage

Run the main script:

```bash
python app.py
```

The menu options:

1. Show all habits
2. Add a habit
3. Delete a habit
4. Mark habit as done
5. View streaks
6. Save and exit

Follow the prompts to manage your habits.

## File Structure

- `app.py` – main program
- `habits.json` – saved habits (created automatically)

## Notes

- Habit fields include: `id` (unique), `name`, `category`, `status`, `created_at`, and `completions`.
- Date format: YYYY-MM-DD.
- Daily streaks are calculated based on consecutive completion dates.
