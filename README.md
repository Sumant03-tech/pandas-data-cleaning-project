# 🧹 Student Data Cleaning Project using Pandas

A beginner-friendly Python project that demonstrates how to clean and preprocess student data using the **Pandas** library. This project covers handling missing values, removing duplicate records, renaming columns, and preparing datasets for analysis.

---

## 🚀 Features

* Create a student dataset using a Pandas DataFrame
* Detect missing values using `isnull()`
* Count missing values
* Remove duplicate records using `drop_duplicates()`
* Fill missing values using the column average with `fillna()`
* Rename columns using `rename()`
* Display the cleaned dataset

---

## 🛠️ Technologies Used

* Python 3
* Pandas

---

## 📂 Project Structure

```text
Student-Data-Cleaning/
│── student_data_cleaning.py
│── README.md
```

---

## ▶️ How to Run

1. Clone this repository.

2. Install Pandas:

```bash
pip install pandas
```

3. Run the program:

```bash
python student_data_cleaning.py
```

---

## 📊 Sample Dataset

| Name    |  Age | Mark |
| ------- | ---: | ---: |
| Sumant  |   20 |   95 |
| None    |   21 |   92 |
| Raja    |   34 |   88 |
| Abhi    |   43 |   85 |
| Pritam  | None | None |
| Prakash | None |   89 |
| Abhi    |   43 |   85 |

---

## 🧹 Data Cleaning Performed

* ✔️ Identified missing values
* ✔️ Counted missing values
* ✔️ Removed duplicate rows
* ✔️ Replaced missing marks with the average score
* ✔️ Renamed the **Mark** column to **Score**

---

## 📚 Learning Outcomes

Through this project, I learned how to:

* Work with Pandas DataFrames
* Detect and handle missing values
* Remove duplicate data
* Clean and prepare datasets
* Perform basic data preprocessing for AI/ML projects

---

## 🔮 Future Improvements

* Fill missing names with default values
* Fill missing ages with the average age
* Load datasets directly from CSV files
* Export the cleaned dataset to a new CSV file
* Add data visualization using Matplotlib

---

## 🎯 Project Goal

The purpose of this project is to practice essential **data cleaning techniques**, which are a crucial part of every Data Science and Machine Learning workflow before building predictive models.

---

⭐ This project is part of my journey to becoming an **AI/ML Engineer**.
