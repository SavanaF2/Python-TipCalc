'''
Savana Fallen
24/09/2023
Desc: This app takes in the users bill and the tip percentage then calculates and displays the tip and total amount due followed by an emoji.
'''

import emoji

class tip_calc():
    bill = int(input("Enter the bill amount: "))
    tip_percentage = int(input("Enter the tip percentage: "))
    #converts the percentage to a decimal
    tip_decimal = tip_percentage / 100
    #calculates the tip amount
    pre_tip = bill * tip_decimal
    #rounds the tip amount to the hundredths place so it fits US currency conventions
    tip = round(pre_tip, 2)
    total = bill + tip
    print (emoji.emojize(f'\nYour tip: {tip} \nYour total: {total} \nThank you for tipping :thumbs_up:'))

if __name__ == '__main__':
    tip_calc()
