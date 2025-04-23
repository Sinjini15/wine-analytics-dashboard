import pandas as pd
import sqlite3


PATH = "/home/smitra16/symrise-etl/data/winemag-data_first150k.csv"
# Load CSV
df = pd.read_csv(PATH)

# Clean column names to avoid SQL issues
df.columns = [c.strip().lower().replace(" ", "_") for c in df.columns]

# Create or overwrite SQLite DB
conn = sqlite3.connect("data/wine_features.db")
df.to_sql("wine_reviews", conn, if_exists="replace", index=False)

print("✔️ Data loaded into SQLite database.")
conn.close()
