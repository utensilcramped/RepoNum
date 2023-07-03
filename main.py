import csv

# Read input CSV file
input_file = 'input.csv'
output_file = 'output.csv'

# Define a function to process the data
def process_data(data):
    # Perform data manipulation here
    for row in data:
        # Modify the data as needed
        row['Age'] = int(row['Age']) + 1

    return data

# Open the input CSV file and read the data
with open(input_file, 'r') as file:
    reader = csv.DictReader(file)
    data = list(reader)

# Process the data
processed_data = process_data(data)

# Open the output CSV file and write the modified data
with open(output_file, 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=reader.fieldnames)
    writer.writeheader()
    writer.writerows(processed_data)

print("Data processing completed. Modified data written to", output_file)
