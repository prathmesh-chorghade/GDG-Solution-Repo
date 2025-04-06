# GDG-Solution-Repo
 
Access to basic healthcare is something many of us take for granted. But in countless underserved communities, especially those in rural and remote areas, people face major barriers to getting even the most essential medical services. These barriers include a severe shortage of hospitals, clinics, trained healthcare professionals, and in many cases, even a basic understanding of preventive care. As a result, preventable diseases go untreated, minor illnesses escalate, and entire communities suffer from reduced quality of life. This situation directly connects to the United Nations Sustainable Development Goal 3, which aims to ensure healthy lives and promote well-being for people of all ages.

To address this problem, we’ve developed a simple but powerful Python-based solution that helps identify where healthcare is most urgently needed. Our tool collects and analyzes healthcare data from different communities across multiple years. The data includes population size, number of doctors, availability of medical facilities, and the number of reported cases of preventable diseases. With this data, we calculate a custom metric called the Healthcare Need Index — a score that helps us measure how underserved a community is.

Here's how it works: we’ve built a backend using SQLite to store and manage healthcare data. The Python script takes input either manually or from existing records, allowing users to update and analyze data year by year. It then uses Pandas for data handling and Seaborn and Matplotlib for visualization. Our script calculates the need index using a formula that considers disease prevalence and subtracts the influence of available medical support like doctors and clinics. This gives us a clear, visual representation of which communities are lacking healthcare access the most.

For example, if a town has a large population, very few doctors, and high disease cases, it will have a much higher need index. These insights are shown in a bar chart that compares communities across different years, making it easier for decision-makers to target their interventions.

By helping identify high-need areas, our solution can assist governments, NGOs, and healthcare organizations in prioritizing where to send medical resources, set up new clinics, or launch awareness campaigns. It's scalable, easy to update, and aligned with global development goals. This is just a first step — but it's a data-driven one, and it brings us closer to a world where everyone, no matter where they live, has access to the healthcare they deserve."


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

Explain this code