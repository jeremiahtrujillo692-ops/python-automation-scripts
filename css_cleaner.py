import pandas as pd

# Load CSV file
file = input("Enter CSV file name: ")
df = pd.read_csv(file)

# Clean data
df = df.drop_duplicates()
df = df.dropna()

# Save cleaned file
df.to_csv("cleaned_data.csv", index=False)

print("Data cleaned and saved as cleaned_data.csv")
