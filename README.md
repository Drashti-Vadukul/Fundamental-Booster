હા 👍 આ **Interactive Personal Data Collector** program માટે README.md નું detailed content, તમારા code પ્રમાણે જ, અને **Author સૌથી પહેલા** રાખીને:

# 👩‍💻 Author

**Drashti Vadukul**

BCA Student | Learning Python, AI, ML & Data Science

---

# 🧑‍💻 Interactive Personal Data Collector

A beginner-friendly **Python console-based project** that collects basic information from the user and displays the collected data along with its **data type and memory address**.

The project also calculates an **approximate birth year** based on the user's age.

---

## 📌 Project Overview

The program interacts with the user by asking for:

* Name
* Age
* Height in meters
* Favourite number

After collecting the information, the program displays each value along with:

* The entered value
* Its Python data type
* Its memory address

Finally, the program calculates the approximate birth year using the entered age.

---

## ✨ Features

### 👤 Personal Information Collection

The program uses `input()` to collect the user's basic information.

It accepts:

* **Name** as a string
* **Age** as an integer
* **Height** as a float
* **Favourite Number** as an integer

---

### 🔍 Data Type Identification

The program uses Python's `type()` function to identify the data type of each collected value.

Example:

```text
Name : Drashti
Type : <class 'str'>

Age : 20
Type : <class 'int'>

Height : 1.65
Type : <class 'float'>
```

---

### 🧠 Memory Address

The program uses Python's `id()` function to display the memory identity/address associated with each object during that program execution.

Example:

```text
Name : Drashti
Memory Address : 123456789
```

This helps beginners understand that Python values are represented by objects in memory.

---

### 🎂 Birth Year Calculation

The program calculates an approximate birth year using:

```python
birth_year = 2026 - age
```

Example:

```text
Age = 20
Birth Year = 2006
```

The result is approximate because the exact birth year depends on whether the user's birthday has already occurred in 2026.

---

## 🧠 Concepts Used

This project demonstrates several important Python fundamentals:

* `print()` – Display output
* `input()` – Take user input
* `int()` – Convert input into an integer
* `float()` – Convert input into a decimal number
* `type()` – Identify data type
* `id()` – Get the object's identity
* Variables – Store user information
* Arithmetic operators – Calculate birth year
* String formatting and output
* Basic user interaction

---

## 🔄 Program Flow

```text
Start
  ↓
Display Welcome Message
  ↓
Enter Name
  ↓
Enter Age
  ↓
Enter Height
  ↓
Enter Favourite Number
  ↓
Display Collected Information
  ↓
Show Data Types
  ↓
Show Memory Addresses
  ↓
Calculate Approximate Birth Year
  ↓
Display Thank You Message
  ↓
End
```

---


## 🛠️ Technologies Used

**Language:** Python

**Project Type:** Console-Based Application

**Difficulty Level:** Beginner

**Editor:** VS Code

---

## 🎯 Learning Objective

The main goal of this project is to understand how Python handles **different types of data and user input**.

Through this project, I practiced:

* Taking and storing user input
* Converting input into different data types
* Understanding Python data types
* Using built-in functions
* Performing basic calculations
* Understanding object identity in Python

---

## 🚀 Future Improvements

The project can be improved by adding:

* Email and phone number collection
* Age validation
* BMI calculation using height
* More personal information fields
* Better formatted output
* Input error handling

---

## 📚 Conclusion

The **Interactive Personal Data Collector** is a simple Python project created to strengthen the fundamentals of **variables, data types, type conversion, built-in functions, user input, and basic calculations**.

It provides practical understanding of how Python accepts, stores, processes, and displays different types of data.

---

## 👩‍💻 Author

**Drashti Vadukul**

BCA Student | Aspiring Data Analyst
Learning Python | AI | ML | Data Science

⭐ *Learning Python fundamentals one project at a time.*


![Program Output](output.png)