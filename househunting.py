annual_salary = int(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = int(input("Enter the cost of your dream home: "))
portion_down_payment = 0.25*total_cost
current_savings = 0
r = 0.04
return_on_investment = current_savings*r/12
portion_saved = portion_saved*annual_salary/12
number_of_months = 0

while current_savings <= portion_down_payment:
    number_of_months = number_of_months + 1
    current_savings = current_savings + portion_saved + current_savings*r/12

print("Number of months: ", number_of_months)