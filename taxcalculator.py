
tax_brackets = [ #upper limits and tax rates
    (158000, 0.15),
    (330000, 0.20),
    (800000, 0.27),
    (4300000, 0.35),
    (float('inf'), 0.40) #more than 4.3 million
]

def get_user_income():
    while True:
        print('Enter your yearly income:  ')
        try:    
            user_income = int(input())
            return user_income
        except ValueError:
            print('Please enter a number.')

def calculate_tax():
    user_income = get_user_income()
    previous_limit = 0 # tracks the lower limit of the income slice being taxed in each bracket
    tax = 0
    for limit, rate in tax_brackets:
        taxable_income = min(user_income, limit) - previous_limit
        if taxable_income > 0:
            tax += taxable_income * rate
        previous_limit = limit
    return f'You must pay {tax:.2f} TL for your income.\nYou have {user_income - tax:.2f} earnings left.'

print('''Attention! This program is only to give you a rough estimation of your
tax debt. For precise and legal calculations, please also consult your accountant.''')

print(calculate_tax())

