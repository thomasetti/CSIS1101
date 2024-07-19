def calculate_fees(base_price):
    """Calculate the additional fees based on the base price."""
    fees = {
        "Additional Dealer Markup": 1000,
        "Processing Fee": 100,
        "Destination Charge": 495,
        "Undercoating": 295,
        "Rust-Proofing": 395,
        "Prep Fee": 250,
        "Sleaze Tax (5%)": 0.05 * base_price,
        "Restocking Fee (12%)": 0.12 * base_price
    }
    return fees

def print_cost_report(car, base_price, fees):
    """Print the cost report with the base price and all additional fees."""
    total_cost = base_price + sum(fees.values())
    
    print(f"\n{car}")
    print(f"{'Base Price:':<30}${base_price:,.2f}")
    for fee, amount in fees.items():
        print(f"{fee:<30}${amount:,.2f}")
    print(f"{'Total Cost:':<30}${total_cost:,.2f}")

def main():
    print("Welcome to Group 4 StealershipSUV, LLC")
    
    car = input("\nWhich car are you interested in? ")
    base_price = float(input(f"\nHow much will you give us for the {car}? "))
    
    fees = calculate_fees(base_price)
    print_cost_report(car, base_price, fees)

if __name__ == "__main__":
    main()