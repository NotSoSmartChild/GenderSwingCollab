import pandas as pd

men_df = pd.read_csv('Main/Statistics/Males.csv')
women_df = pd.read_csv('Main/Statistics/Females.csv')
total_df = pd.read_csv('Main/Statistics/Persons.csv')

# Assuming the LGA column is named 'lga'
merged_df = men_df.merge(women_df, on='LGA').merge(total_df, on='LGA')
merged_df['gender_diff'] = (merged_df['Males'] - merged_df['Females']) / merged_df['Persons']

# Save the gender difference data as a new CSV file
gender_diff_df = merged_df[['LGA', 'gender_diff']]
gender_diff_df.to_csv('gender_diff.csv', index=False)

print("Men data columns:", men_df.columns)
print("Women data columns:", women_df.columns)
print("Total data columns:", total_df.columns)