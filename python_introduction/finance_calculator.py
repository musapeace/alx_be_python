# calculating monthly user income salary
monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your total monthly expenses: "))

# calculating monthly savings
monthly_savings = int(monthly_income) - int(monthly_expenses)
print(f"Your monthly savings are {monthly_savings} ")

# project annual savings:
projected_savings = float(monthly_savings * 12) + float(monthly_savings * 12 * 0.05)
print(f"Projected savings after one year , with interest , is : {projected_savings} ")