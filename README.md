# 🍷 Wine Analytics Dashboard

This project analyzes 10,000 wine reviews by variety, country, price, and rating to uncover trends in wine quality and market preferences. Built as part of a data storytelling and analytics exercise to strengthen skills in ETL, data visualization, and dashboard design.

---

## 📊 Features

- **Exploratory Analysis** of 10,000 wine reviews
- **Interactive Tableau Dashboard**: filterable by country, variety, score range
- **Visualizations** include:
  - Average Points by Country
  - Price vs. Points Scatter Plot
  - Top 10 Most Reviewed Varieties
- **ETL & Preprocessing**: done using Python, PySpark, and SQL (SQLite)
- **CI/CD-ready structure** for reproducible workflows

---

## 🔗 Live Dashboard

👉 [View the Tableau Dashboard]([https://public.tableau.com/app/profile/sinjini.mitra/viz/WineReviewInsightsDashboardPricePointsandPopularVarieties/Dashboard1])

---

## 🧰 Tools & Technologies

- Python (pandas, matplotlib, sqlite3)
- Tableau Public
- Git / GitHub
- PySpark (optional ETL extension)
- SQL (SQLite3)

---

## 📁 Project Structure

├── data # Cleaned data 
├── Scripts # Optional modeling extension (e.g., churn/recsys) 
├── 02_feature_modeling.sql (.sql file to combine tables)
├── README.md # You are here



---

## 🚀 Getting Started

To run the local scripts:

1. Clone the repo:
```bash
git clone https://github.com/YOUR_USERNAME/wine-analytics-dashboard.git
cd wine-analytics-dashboard
```
2. Create SQLite DB

   ```sqlite3 wine_reviews.db < create_tables.sql```

