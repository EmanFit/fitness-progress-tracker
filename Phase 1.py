import csv
import datetime
import matplotlib.pyplot as plt

DATA_FILE = "progress.csv"

def log_progress():
    date = datetime.date.today().isoformat()
    weight = input("Enter your weight (kg): ")
    workout = input("Enter workout type: ")

    with open(DATA_FILE, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, weight, workout])
    print("Progress saved!")

def show_chart():
    dates, weights = [], []
    try:
        with open(DATA_FILE, mode="r") as file:
            reader = csv.reader(file)
            for row in reader:
                dates.append(row[0])
                weights.append(float(row[1]))

        plt.plot(dates, weights, marker="o")
        plt.xlabel("Date")
        plt.ylabel("Weight (kg)")
        plt.title("Fitness Progress")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
    except FileNotFoundError:
        print("No data found. Log progress first!")

while True:
    print("\n1. Log Progress")
    print("2. Show Chart")
    print("3. Exit")
    choice = inpnut("Choose an option: ")

    if choice == "1":
        log_progress()
    elif choice == "2":
        show_chart()
    elif choice == "3":
        break
    else:
        print("Invalid choice!")
        
