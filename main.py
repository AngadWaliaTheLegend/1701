
age= int(input("enter current age in years:"))
years_of_service= int(input("enter current years of service:"))
income1= int(input("enter the largest expected annual income:"))
income2= int(input("enter the second-largest expected annual income:"))
income3= int(input("enter the third-largest expected annual income:"))

average_of_best_3_annual_incomes= (income1 + income2 + income3)/3
rate=1.4/100



retirement55 = int(55)
retirement60= int(60)
retirement65 = int(65)

years_experience_at_retirement55 = retirement55 -age + years_of_service
years_experience_at_retirement60 = retirement60 -age + years_of_service
years_experience_at_retirement65 = retirement65 -age + years_of_service


pension_income55 = average_of_best_3_annual_incomes * rate * years_experience_at_retirement55
print(pension_income55)
pension_income60 = average_of_best_3_annual_incomes * rate * years_experience_at_retirement60
print(pension_income60)
pension_income65 = average_of_best_3_annual_incomes * rate * years_experience_at_retirement65
print(pension_income65)


print(f"{"retirement age"}{}")