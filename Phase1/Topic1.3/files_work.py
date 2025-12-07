
# Writing to a file (overwrite)
with open("output.txt", "w") as file:
    file.write("Hello, Dhruvi! Welcome to Python file handling.")

with open("output.txt", "a") as file:
    file.write("\nHello, Dhruvi! Welcome to Python file handling.")
    # file.write("\nHello, Dhruvi! Welcome to Python file handling.")
    # file.write("\nHello, Dhruvi! Welcome to Python file handling.")

with open("output.txt", "r") as file:
    # content = file.read()
    print(file.read())

import csv

# Writing data to a CSV file

with open("expenses.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Date", "Category", "Amount"])  # Header
    writer.writerow(["2025-12-01", "Food", 20.50])
    writer.writerow(["2025-12-02", "Transport", 15.00])
    writer.writerow(["2025-12-03", "Entertainment", 10.00])
    writer.writerow(["2025-12-04", "Shopping", 50.00])
    writer.writerow(["2025-12-05", "Utilities", 75.00])
    writer.writerow(["2025-12-06", "Food", 30.00])
    writer.writerow(["2025-12-07", "Transport", 20.00])
    writer.writerow(["2025-12-08", "Entertainment", 25.00])
    writer.writerow(["2025-12-09", "Shopping", 60.00])
    writer.writerow(["2025-12-10", "Utilities", 100.00])

with open("expenses.csv", mode="r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)