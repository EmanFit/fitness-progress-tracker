import csv
import datetime
import os

DATA_FILE = "fitness_data.csv"

# 🗂️ Initialize CSV file if not exists
def initialize_file():
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Weight (kg)", "Workout", "Steps", "Notes"])

# 📝 Log daily entry
def log_entry():
    date = datetime.date.today().isoformat()
    weight = input("Enter your weight (kg): ")
    workout = input("Describe your workout (e.g., pushups, squats): ")
    steps = input("Enter steps walked today: ")
    notes = input("Any notes or mood? ")

    with open(DATA_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, weight, workout, steps, notes])
    print("✅ Entry saved!")

# 📊 Show weekly summary
def weekly_summary():
    today = datetime.date.today()
    week_ago = today - datetime.timedelta(days=7)
    entries = []

    with open(DATA_FILE, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            entry_date = datetime.date.fromisoformat(row["Date"])
            if entry_date >= week_ago:
                entries.append(row)

    if not entries:
        print("No entries in the past week.")
        return

    print("\n📅 Weekly Summary:")
    total_steps = 0
    total_weight = 0
    count = 0

    for entry in entries:
        print(f"{entry['Date']}: {entry['Workout']} | {entry['Weight (kg)']}kg | {entry['Steps']} steps")
        total_steps += int(entry["Steps"])
        total_weight += float(entry["Weight (kg)"])
        count += 1

    avg_weight = total_weight / count
    print(f"\n📈 Average Weight: {avg_weight:.2f} kg")
    print(f"🚶‍♀️ Total Steps: {total_steps}")

# 🧹 Reset data (optional)
def reset_data():
    confirm = input("Are you sure you want to delete all data? (yes/no): ")
    if confirm.lower() == "yes":
        os.remove(DATA_FILE)
        initialize_file()
        print("🗑️ Data reset complete.")
    else:
        print("Cancelled.")

# 🧭 Main menu
def main():
    initialize_file()
    while True:
        print("\n=== Fitness Progress Tracker ===")
        print("1. Log today's entry")
        print("2. View weekly summary")
        print("3. Reset all data")
        print("4. Exit")

        choice = input("Choose an option (1–4): ")
        if choice == "1":
            log_entry()
        elif choice == "2":
            weekly_summary()
        elif choice == "3":
            reset_data()
        elif choice == "4":
            print("👋 Stay consistent, EMAN! See you tomorrow.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()


