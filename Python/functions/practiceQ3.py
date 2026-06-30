"""
write a function tax_collector(income)
that takes annual_income
returns the tax amount based on these slabs:
up to 2,50,000 - no tax
2,50,000 - 5,00,000 - 5%
5,00,001 - 10,00,000 - 20%
above 10,00,000 - 30%

"""
def tax_collector(annual_income): 
    if annual_income >= 1000000:
        return (30/100) * annual_income
    elif annual_income < 1000000 and annual_income >= 500000:
        return (20/100) * annual_income
    elif annual_income < 500000 and annual_income >= 250000:
        return (5/100) * annual_income
    else:
        return 0
    
result1 = tax_collector(76450)
result2 = tax_collector(345679)
result3 = tax_collector(654567)
result4 = tax_collector(1189765)
print(result1)
print(result2)
print(result3)
print(result4)