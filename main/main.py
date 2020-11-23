# Get percentage of total price
def price_with_tip(billamt, tip, people):
    tip = (tip / 100) + 1
    return (billamt / people) * tip


print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? $"))
tip = int(input(
    "What percentage tip would you like to give? 10, 12, or 15? "))

amount_of_people = int(input("How many people to split the bill? "))
final_amount = round(price_with_tip(total_bill, tip, amount_of_people), 2)

print(f"The total price per person is ${final_amount}")
