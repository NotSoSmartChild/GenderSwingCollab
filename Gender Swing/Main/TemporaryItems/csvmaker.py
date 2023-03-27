import csv

# Path to the CSV files
Males_file = 'Main/Statistics/Males.csv'
Females_file = 'Main/Statistics/Females.csv'
Persons_file = 'Main/Statistics/Persons.csv'

# Path to the output CSV file
output_file = 'gender_diff.csv'

# Dictionary to store population data for each LGA
population_data = {}

# Read in population data for men
with open(Males_file) as csvfile:
    reader = csv.DictReader(csvfile)
    next(reader)  # skip header row
    for row in reader:
        lga = row['lga'].replace(' ', '_')
        if lga not in population_data:
            population_data[lga] = {}
        population_data[lga]['Males'] = int(row['Males'])

# Read in population data for women
with open(Females_file) as csvfile:
    reader = csv.DictReader(csvfile)
    next(reader)  # skip header row
    for row in reader:
        lga = row['lga']
        if lga in population_data:
            population_data[lga]['Females'] = int(row['Females'])

# Read in total population data
with open(Persons_file) as csvfile:
    reader = csv.DictReader(csvfile)
    next(reader)  # skip header row
    for row in reader:
        lga = row['lga']
        if lga in population_data:
            population_data[lga]['Persons'] = int(row['Persons'])

# Calculate gender difference for each LGA and write to output file
with open(output_file, 'w', newline='') as csvfile:
    fieldnames = ['lga', 'Gender Difference']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()

    for lga, data in population_data.items():
        males = data['Males']
        females = data['Females']
        total = data['Persons']

        if total > 0:
            gender_diff = (males - females) / total
            writer.writerow({'lga': lga, 'Gender Difference': gender_diff})

