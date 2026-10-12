
# Student Marks Calculator

# Passing rule: Minimum 35 marks in each subject (out of 100)

name = input("Enter student name: ")

mark1 = int(input("Enter marks in Subject 1: "))
mark2 = int(input("Enter marks in Subject 2: "))
mark3 = int(input("Enter marks in Subject 3: "))

# Calculate total, average, and percentage
total = mark1 + mark2 + mark3
average = total / 3
percentage = (total / 300) * 100

# Display results
print("\n--- Student Marks Report ---")
print("Student Name:", name)
print("Total Marks:", total, "/ 300")
print("Average:", round(average, 2))
print("Percentage:", round(percentage, 2), "%")

# Check pass or fail
if mark1 >= 35 and mark2 >= 35 and mark3 >= 35:
    print("Result: PASS")
else:
    print("Result: FAIL")
