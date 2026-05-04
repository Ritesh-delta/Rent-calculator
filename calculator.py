##input we need from the user 
# total rent
# total electricity bill
# total water bill 
# vegetable we buy from the market 
# grocery that we order 
# total number of people in the house 
# food order from/snacks online 
# output 
# total expense per person

# =========== list of categories where we spent the money  in a month ************
 
rent= float(input("Enter your flat rent = "))
food= float(input("Enter the amount of food ordered = "))
electricity_bill= float(input("Enter the amount of electricity bill = "))
# WATER BILL CALCULATION
water_units = float(input("Enter the number of water units consumed = "))
rate_per_unit = float(input("Enter the rate per unit of water = "))
water_bill = water_units * rate_per_unit

# VEGETALE AND GROCERY CALCULATION
vegetable = float(input("enter the amount of vegetable bought from the market ="))
grocery = float(input("enter the amount of grocery bought from the market ="))

# total number of people in the house 
total_people = int(input("enter the total number of people in the house ="))
# total bill calculation
total_expense = rent + food + electricity_bill + water_bill + vegetable + grocery
expense_per_person = total_expense / total_people
print(f"Total expense per person = ₹{round(expense_per_person,2)}")
