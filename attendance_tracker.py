
import csv
import os

FILE_NAME = "attendance.csv"


# Load attendance records from CSV file
def load_records():
    records = {}

    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r", newline="") as file:
            reader = csv.DictReader(file)

            for row in reader:
                records[row["Name"]] = row["Status"]

    return records


# Save attendance records to CSV file
def save_records(records):
    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Status"])

        for name, status in records.items():
            writer.writerow([name, status])


# Display attendance list
def display_records(records):
    if not records:
        print("No attendance records found.")
        return

    print("\n--- Student Attendance List ---")
    print("Name\t\tStatus")

    for name, status in records.items():
        print(f"{name}\t\t{status}")


# Calculate attendance percentage
def calculate_percentage(records):
    if not records:
        print("No attendance records available.")
        return

    total = len(records)
    present = sum(1 for status in records.values()
                  if status == "Present")

    percentage = (present / total) * 100

    print("Total Students:", total)
    print("Present:", present)
    print("Absent:", total - present)
    print("Attendance Percentage:", round(percentage, 2), "%")


# Main program
records = load_records()

while True:
    print("\n===== STUDENT ATTENDANCE TRACKER =====")
    print("1. Add Student and Mark Attendance")
    print("2. Display Attendance")
    print("3. Calculate Attendance Percentage")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ").strip()

        if not name:
            print("Student name cannot be empty.")
            continue

        print("1. Present")
        print("2. Absent")

        status_choice = input("Enter attendance status: ")

        if status_choice == "1":
            records[name] = "Present"
        elif status_choice == "2":
            records[name] = "Absent"
        else:
            print("Invalid attendance choice.")
            continue

        save_records(records)
        print("Attendance saved successfully!")

    elif choice == "2":
        display_records(records)

    elif choice == "3":
        calculate_percentage(records)

    elif choice == "4":
        save_records(records)
        print("Attendance records saved. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
