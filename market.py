import pandas as pd


#df=pd.read_csv("Marketing and Conversion Analytics/data/2019-Nov.csv",nrows=1000000)
chunks = []
file_path="Marketing and Conversion Analytics/data/2019-Nov.csv"
# Read the file in 5-million-row batches
for chunk in pd.read_csv(file_path, chunksize=5000000):
    # Randomly keep 2% of rows from each batch to span the whole month evenly
    sample_chunk = chunk.sample(frac=0.02, random_state=42)
    chunks.append(sample_chunk)

# Combine them all into one dataframe
df = pd.concat(chunks, axis=0)
print(f"Successfully sampled {len(df)} rows across all of November!")

#data structure
print("Shape:",df.shape)
print("First five:",df.head())
print("Info:",df.info())
print("Columns:",df.columns)
print("Datatypes:",df.dtypes)
print("Memory usage:",df.memory_usage(deep=True))

#cleaning data
print(df.isnull().sum())
print(df.duplicated().sum())

#drop duplicates
initial_rows=len(df)
df=df.drop_duplicates()
final_rows=len(df)
print(f"Removed {initial_rows-final_rows} duplicates")

#filling missing value
df['category_code']=df["category_code"].fillna("Unknown")
df['brand']=df["brand"].fillna("Unknown")

#changing type
df['event_time']=df["event_time"].str.replace('UTC','',case=False)
df['event_time']=pd.to_datetime(df['event_time'])

# Keep only the first part of category code
df['category_short'] = df['category_code'].str.split('.').str[0].str.title()


print("Dataset Cleaned!")

output_path="market_df.csv"
df.to_csv(output_path,index=False)
print("Export Completed!")

import os
print(os.getcwd())