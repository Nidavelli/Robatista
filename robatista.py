from rich import print
from datetime import datetime

# Get current date and time
print(datetime.now().strftime("%d/%m/%Y, %H:%M:%S"))

# Get customer details
person_details = {
    "first_name": input("What is your first name?\n"),
    "last_name": input("What is your last name?\n")
}
full_name = f"{person_details['first_name']} {person_details['last_name']}"

print(f"\n\nHello, {full_name}!")
print("Welcome to Nida's Coffee Barista Special!!!!\n")

# Menu options
menu_list = {"Black Coffee", "Espresso", "Latte", "Cappucino"}

while True:
    coffee = input(f"{person_details['first_name']}, what would you like from our menu today?\n Here is what we are serving: \n{menu_list}\n\n")
    if coffee in menu_list:
        break
    else:
        print("\nSorry, we don't have that on our menu. Please choose from the options above\n\n")

# Get coffee quantity
coffee_quantity = int(input(f"\n\nHow many {coffee} coffee's would you like?\n"))
total_price = coffee_quantity * 60

print(f"\n\nSounds great {full_name}, we'll have the {coffee_quantity} {coffee}s ready for you in a moment.\n")

# Special requests
special_requests = input("\n\nWould you like any special requests (e.g. extra sugar, cream)?\n\n")
if special_requests:
    print(f"\n\nGot it! We'll make sure to add {special_requests} to your order")

# Payment options
payment_options = {"Cash", "Card", "Mobile Payment"}
payment_method = input(f"\nHow would you like to pay?\n {payment_options}\n")
while payment_method not in payment_options:
    print("Sorry, we don't accept that payment method. Please choose from the options above")
    payment_method = input(f"\nHow would you like to pay?\n {payment_options}\n")

# Order summary
print("\n[bold]Order Summary[/bold]\n")
print(f"Coffee: {coffee}\nQuantity: {coffee_quantity}\nTotal Price: {total_price} Ksh\n")

# Loyalty program
loyalty_program = input(f"\nAre you a loyalty program member? (y/n)\n")
if loyalty_program.lower() == 'y':
    print("Thank you for being a loyal customer! You'll receive 10% off your order.")
    total_price *= 0.9

print(f"\n\nYour total bill is: {total_price:.2f} Ksh")