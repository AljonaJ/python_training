salary = float(input('Please enter your salary:'))

unemployment_insurance = salary * 1.6 / 100
funded_pension = salary * 2 / 100

if salary <= 1200:
    tax_free_income = 500
elif 1200 < salary < 2100:
    tax_free_income = 500 - 0.55556 * (salary - 1200)
else:
    tax_free_income = 0

income_tax = (salary - tax_free_income - unemployment_insurance - funded_pension) * 0.2
net_salary = salary - income_tax - unemployment_insurance - funded_pension

print('Your net salary is', net_salary)
print(
    'Taxes:',
    '\nUnemployment insurance =', unemployment_insurance,
    '\nFunded pension =', funded_pension,
    '\nIncome tax =', income_tax
)
