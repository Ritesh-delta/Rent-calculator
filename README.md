# 🏠 Rent Calculator (Python)

A simple and useful Python project to calculate **per-person living expenses** in a shared house.
This tool helps split rent, food, electricity, water, and grocery costs equally among all members.

---

## 🚀 Features

* Calculates total household expenses
* Splits expenses equally among all people
* Includes:

  * 🏠 Rent
  * 🍽️ Food
  * ⚡ Electricity bill
  * 💧 Water bill (based on units)
  * 🥦 Vegetables
  * 🛒 Groceries
* Clean and beginner-friendly Python code

---

## 🧠 How It Works

1. User inputs all expenses
2. Water bill is calculated separately:

   ```
   water_bill = water_units × rate_per_unit
   ```
3. All expenses are added
4. Total is divided by number of people

---

## 💻 Code

```python
rent = float(input("Enter your flat rent = "))
food = float(input("Enter the amount of food ordered = "))
electricity_bill = float(input("Enter the amount of electricity bill = "))

# Water bill calculation
water_units = float(input("Enter the number of water units consumed = "))
rate_per_unit = float(input("Enter the rate per unit of water = "))
water_bill = water_units * rate_per_unit

# Vegetable and grocery
vegetable = float(input("Enter the amount of vegetables bought = "))
grocery = float(input("Enter the amount of groceries bought = "))

# Number of people
total_people = int(input("Enter total number of people = "))

# Total calculation
total_expense = rent + food + electricity_bill + water_bill + vegetable + grocery

if total_people > 0:
    expense_per_person = total_expense / total_people
    print(f"Total expense per person = ₹{round(expense_per_person, 2)}")
else:
    print("Number of people must be greater than 0")
```

---

## ▶️ How to Run

1. Clone the repository:

   ```
   git clone https://github.com/Ritesh-delta/Rent-calculator.git
   ```

2. Navigate to the folder:

   ```
   cd Rent-calculator
   ```

3. Run the program:

   ```
   python calculator.py
   ```

---

## 📸 Sample Output

```
Enter your flat rent = 10000
Enter the amount of food ordered = 2000
Enter the amount of electricity bill = 1500
Enter the number of water units consumed = 100
Enter the rate per unit of water = 2
Enter the amount of vegetables bought = 800
Enter the amount of groceries bought = 1200
Enter total number of people = 4

Total expense per person = ₹3875.0
```

---

## 🛠️ Future Improvements

* Add GUI using Tkinter or Web App using Flask
* Save monthly expense history
* Split expenses unevenly (custom share)
* Add categories & charts

---

## 🤝 Contributing

Contributions are welcome!
Feel free to fork this repo and improve the project.

---

## 📄 License

This project is open-source and free to use.

---

## 👨‍💻 Author

**Ritesh Yadav**
GitHub: https://github.com/Ritesh-delta

---

⭐ If you like this project, don't forget to star the repo!
