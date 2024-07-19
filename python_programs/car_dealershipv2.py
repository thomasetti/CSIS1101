#Display Welcome Message
print("Welcome to Group 4 Stealership")
#Get car and price from customer
car_name = input("Which car would you like to buy? ")
base_price = float(input(f"How much do you want to spend for the {car_name}? "))
#Fees
additional_dealer_markup = 1000
processing_fee = 100
destination_charge = 495
undercoating = 295
rust_proofing = 395
prep_fee = 250
sleaze_tax = 0.05 * base_price
restocking_fee = 0.12 * base_price
#Calculate total cost
total_cost = (
    base_price
    + additional_dealer_markup
    + processing_fee
    + destination_charge
    + undercoating
    + rust_proofing
    + prep_fee
    + sleaze_tax
    + restocking_fee
)
#Print pricing
print(f"Here is the deal on the {car_name}: ")
print(f"{'Base Price:':<25} ${base_price:,.2f}")
print(f"{'Additional Dealer Markup:':<25} ${additional_dealer_markup:,.2f}")
print(f"{'Processing Fee:':<25} ${processing_fee:,.2f}")
print(f"{'Destination Charge:':<25} ${destination_charge:,.2f}")
print(f"{'Undercoating:':<25} ${undercoating:,.2f}")
print(f"{'Rust-Proofing:':<25} ${rust_proofing:,.2f}")
print(f"{'Prep Fee:':<25} ${prep_fee:,.2f}")
print(f"{'Sleaze Tax:':<25} ${sleaze_tax:,.2f}")
print(f"{'Restocking Fee:':<25} ${restocking_fee:,.2f}")
print(f"{'Total Cost:':<25} ${total_cost:,.2f}")
