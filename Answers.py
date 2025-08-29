
# Week 3 Assignment - Discount Calculator

def calculate_discount(price, discount_percent):
    
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Main program
def main():
    print("=== Discount Calculator ===")
    
    # Get user input
    try:
        original_price = float(input("Enter the original price of the item: $"))
        discount_percentage = float(input("Enter the discount percentage: "))
        
        # Calculate the final price using the function
        final_price = calculate_discount(original_price, discount_percentage)
        
        # Display results
        if discount_percentage >= 20:
            savings = original_price - final_price
            print(f"\nDiscount applied! ({discount_percentage}%)")
            print(f"Original price: ${original_price:.2f}")
            print(f"You saved: ${savings:.2f}")
            print(f"Final price: ${final_price:.2f}")
        else:
            print(f"\nNo discount applied (discount must be 20% or higher)")
            print(f"Final price: ${final_price:.2f}")
            
    except ValueError:
        print("Error: Please enter valid numbers for price and discount percentage.")

# Run the program
if __name__ == "__main__":
    main()