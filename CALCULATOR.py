# SET THE LIMIT OF THE TAX BRACKETS
LIM_1=10164
LIM_2=19740
LIM_3=29316
LIM_4=38892

# TAX RATES
rat1=0.1
rat2=0.15
rat3=0.2
rat4=0.25
rat5=0.30
# prompt the user to read the income of an employee
income=float(input("Enter your income:"))
# compute the amount of tax payable
if income <LIM_1:
    tax=rat1*income
elif income < LIM_2:
    tax=rat1*LIM_1+rat2*(income-LIM_1)
elif income < LIM_3:
    tax=rat1*LIM_1+rat2*(LIM_2-LIM_1)+rat3*(income-LIM_2)
elif income < LIM_4:
    tax=rat1*LIM_1+rat2*(LIM_2-LIM_1)+rat3*(income-LIM_2)+rat4*(income-LIM_3)
else: tax=rat1*LIM_1+rat2*(LIM_2-LIM_1)+rat3*(income-LIM_2)+rat4*(income-LIM_3)+rat5*(income-LIM_4)

# Display the results
# simple math for calculations
tax_relief =1162
house_allowance=15000
payee=tax-tax_relief
basic_salary=income-house_allowance
cop_deduction= 0.05*basic_salary
deduction=payee+cop_deduction
net_pay =income-deduction

print("on an income of Kes"+ format (income,",.2f"),
      "the tax payable is Kes"+ format(payee,",.2f"),
      "the basic salary is Kes"+format(basic_salary,",.2f"),
      "the cooperative deduction is Kes"+format(cop_deduction,",.2f"),
      "The total deduction is Kes"+ format(deduction,",.2f"),
      "the net_pay is Kes"+format(net_pay,",.2f")+'.')




