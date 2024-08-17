import pandas as pd

# Load the CSV file into a DataFrame
file_path = r'C:\Users\Siris\Desktop\GitHub Projects 100 Days NewB\_24_0078__Day74_Aggregate_and_Merge_Data_w_Pandas__240814\NewProject\r00-r09 START\r00_env_START\data\themes.csv'
df = pd.read_csv(file_path)

# Filter the DataFrame to find occurrences of 'Star Wars'
star_wars_df = df[df['name'] == 'Star Wars']

# Display the first few rows of the filtered DataFrame
print(star_wars_df.head())

# Display the count of 'Star Wars'
star_wars_count = star_wars_df.shape[0]
print(f"\nThe theme 'Star Wars' appears {star_wars_count} times in the themes.csv file.")
