import csv

def read_csv_file(file_path):
    try:
        with open(file_path, mode='r') as file:
            reader = csv.reader(file)
            # Assuming the first row contains headers
            headers = next(reader)
            print("Headers:", headers)
            
            for row in reader:
                print(row)
    except FileNotFoundError:
        print("Oops! The file was not found. Please check the file path.")
    except csv.Error as e:
        print(f"Oops! There was an error reading the CSV file. Please check the file format.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("Attempted to read the file.")

def main():
    file_path = input("Enter the path to the CSV file: ")
    read_csv_file(file_path)

if __name__ == "__main__":
    main() 