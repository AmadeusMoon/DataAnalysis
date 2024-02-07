# Calculate tax based on income
def calculate_taxes(brackets, rates, income: int = None):

    # Define income if undefined
    if income is None:
        income = 0
    else:
        remaining_income = income
        tax = 0

    for i in range(len(brackets)):
        if remaining_income > brackets[i]:
            tax += brackets[i] * rates[i]
            remaining_income -= brackets[i]
        else:
            tax += remaining_income * rates[i]
            break

    return tax
