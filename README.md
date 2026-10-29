# CodeAlpha Web Scraping & Analysis Project

## Project Overview
This project is part of the **CodeAlpha Data Analytics Internship**.  
It covers **Task 1 (Web Scraping)** and **Task 2 (Exploratory Data Analysis)**.

I scraped book data from an online bookstore and performed basic exploratory analysis on the collected dataset.

---

## Tools & Technologies Used
- Python
- BeautifulSoup
- Requests
- CSV module

---

## Project Structure
- `scrape_books.py` → Web scraping script
- `eda_books.py` → Exploratory Data Analysis script
- `books_data.csv` → Raw scraped data
- `books_data_cleaned.csv` → Cleaned version of the data (if available)

---

## Web Scraping Summary
I used Python with BeautifulSoup and Requests to extract the following information from the website:

- Book Title
- Price
- Rating
- Availability

I scraped multiple pages and saved the data into a CSV file.

---

## Exploratory Data Analysis (EDA) Summary

**Key Findings from EDA:**

- The dataset contains **100 books**.
- Columns available: Title, Price, Rating, and Availability.
- Rating Distribution is quite balanced:
  - Rating 1: 22 books
  - Rating 2: 19 books
  - Rating 3: 22 books
  - Rating 4: 18 books
  - Rating 5: 19 books
- All 100 books are **In Stock**.
- No missing values were found.
- The data is clean and ready for visualization.

---

## How to Run the Project

1. Install the required libraries:
```bash
pip install requests beautifulsoup4

## Author
Okolie Ifeanyi Emmanuel
CodeAlpha Intern
