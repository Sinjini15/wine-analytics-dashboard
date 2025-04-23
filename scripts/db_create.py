import sqlite3

# Creates the file if it doesn't exist
conn = sqlite3.connect("wine_features.db")
conn.close()
