# Calculate tax based on income
def calculate_taxes(brackets, rates, income: int):

    remaining_income = income
    tax = 0

    for i in range(len(brackets)):
        if remaining_income <= brackets[i]:
            tax += remaining_income * rates[i]
            break
        else:
            tax += brackets[i] * rates[i]
            remaining_income -= brackets[i]

    # Add tax for income over the highest bracket
    if remaining_income > 0:
        tax += remaining_income * rates[-1]

    return tax
