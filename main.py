business_name = "yusuf and sons"
principal = float(input("Enter initial principal amount: "))
Interest_rate = float(input("enter interest rate (as a decimal):"))
times_compounded = int(input("enter number of times interest is compounded per time period: "))
time_periods = int(input("enter number of time periods: "))
simple_interest = principal * (1 + Interest_rate * time_periods)
compound_interest = principal * (1 + Interest_rate / times_compounded) ** (times_compounded * time_periods)
print(f"Business Names: (business_name)")
print(f"Simple Interest: (simple_interest:.2f)")
