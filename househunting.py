annual_salary = int(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
annual_rate_of_return = float(input("Enter the expected annual rate of return: "))
total_cost = int(input("Enter the cost of your dream home: "))
percent_down_payment = float(input("Enter the percent of your home's cost to save as a down payment: "))
current_savings = 0
portion_saved = portion_saved*annual_salary/12
number_of_months = 0

if annual_rate_of_return != 0.04:
    r = float(annual_rate_of_return)
else:
    r = 0.04    

return_on_investment = current_savings*r/12

if percent_down_payment != 0.25:
    portion_down_payment = percent_down_payment*total_cost
else: 
    portion_down_payment = 0.25*total_cost

while current_savings <= portion_down_payment:
    number_of_months = number_of_months + 1
    return_on_investment = current_savings*r/12
    current_savings = current_savings + portion_saved + return_on_investment

print("Number of months: ", number_of_months)