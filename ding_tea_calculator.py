print("Welcome to calculator!")
default_money= str(input("The amount available in the cash register today is $80, correct? (Yes or No)\n")).lower()
amount_money= float(input("Enter the total money amount? \n"))
amount_tips= float(input("Enter the total money tips amount? \n"))
cash_register= float(input("Enter the total cash in the cash register? \n"))
cash_tips = float(input("Enter the total cash tips amount? \n"))
tips_sheare= int(input("How many people will share tips? \n"))
tips_tax_deductions = amount_tips - float(amount_tips*15/100)
if default_money == "yes":
    total_money= amount_money - 80 - tips_tax_deductions
    dollars_left = int(total_money) - int(cash_register)
    if total_money > cash_register:
        print(f"You have ${dollars_left} left over")
    elif total_money == cash_register:
        total_tips = cash_tips + tips_tax_deductions
        tips_each_person = total_tips / tips_sheare
        print("The amount in the cash register is correct!")
        print(f"The tip each person received is ${tips_each_person}")
    else:
        print(f"Something's wrong here; you're $ {dollars_left} short.")
elif default_money == "no":
    default_money_new= int(input("Enter the amount available in the cash register today? \n"))
    total_money= amount_money - default_money_new - tips_tax_deductions
    dollars_left = int(total_money) - int(cash_register)

    if total_money > cash_register:
        print(f"You have ${dollars_left} left over")
    elif total_money == cash_register:
        print("The amount in the cash register is correct!")
        total_tips = cash_tips + tips_tax_deductions
        tips_each_person = total_tips / tips_sheare
        print(f"The tip each person received is ${tips_each_person}")
    else:
        print(f"Something's wrong here; you're $ {dollars_left} short.")
else:
    print("Oh no, something is wrong!")
