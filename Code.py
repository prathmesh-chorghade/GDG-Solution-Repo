import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Connect to SQLite database (or create it)
conn = sqlite3.connect("healthcare_data.db")
cursor = conn.cursor()

# Create a table to store community healthcare data
cursor.execute('''
CREATE TABLE IF NOT EXISTS healthcare_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    community TEXT,
    year INTEGER,
    population INTEGER,
    medical_facilities INTEGER,
    doctors INTEGER,
    preventable_diseases INTEGER
)
''')
conn.commit()

# Function to insert new data
def insert_data():
    print("\n--- Insert New Community Healthcare Data ---")
    community = input("Community Name: ")
    year = int(input("Year: "))
    population = int(input("Population: "))
    medical_facilities = int(input("Number of Medical Facilities: "))
    doctors = int(input("Number of Doctors: "))
    preventable_diseases = int(input("Reported Preventable Disease Cases: "))
    
    cursor.execute('''
    INSERT INTO healthcare_data (community, year, population, medical_facilities, doctors, preventable_diseases)
    VALUES (?, ?, ?, ?, ?, ?)
    ''', (community, year, population, medical_facilities, doctors, preventable_diseases))
    conn.commit()
    print("✅ Data inserted successfully!")

# Function to analyze and visualize data
def analyze_data():
    print("\n--- Analyzing Healthcare Needs ---")
    df = pd.read_sql_query("SELECT * FROM healthcare_data", conn)
    if df.empty:
        print("No data available.")
        return

    print("\n📊 Healthcare Data (Last Few Years):")
    print(df)

    # Calculate healthcare need index (custom metric)
    df['need_index'] = (df['preventable_diseases'] / df['population']) * 1000 - (df['doctors'] + df['medical_facilities']) * 0.5

    # Visualize need index
    plt.figure(figsize=(10, 6))
    sns.barplot(data=df, x='community', y='need_index', hue='year')
    plt.title("Healthcare Need Index by Community")
    plt.ylabel("Need Index (Higher = More Need)")
    plt.xlabel("Community")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Main menu
def main():
    while True:
        print("\n--- Healthcare Access Analyzer ---")
        print("1. Insert New Data")
        print("2. Analyze & Visualize Data")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            insert_data()
        elif choice == '2':
            analyze_data()
        elif choice == '3':
            break
        else:
            print("❌ Invalid choice. Try again.")

    conn.close()

if _name_ == "_main_":
    main()