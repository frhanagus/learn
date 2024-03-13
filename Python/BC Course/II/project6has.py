#Project 6 : Shipping Cost Calculator

def calculate_shipping_cost(weight, distance, shipping_method):
    base_rate_standard = 5.00
    base_rate_express = 15.00
    rate_per_pound = 2.00
    rate_per_mile = 0.50
    
    if shipping_method == "Standard":
        base_rate = base_rate_standard
    elif shipping_method == "Express":
        base_rate = base_rate_express
    else:
        print("Invalid shipping method.")
        return
    
    total_cost = base_rate + (rate_per_pound * weight) + (rate_per_mile * distance)
    
    if weight > 10:
        total_cost *= 0.9
    if distance > 500:
        total_cost *= 0.8
    
    return total_cost

def main():
    weight = float(input("Enter the package weight in pounds: "))
    distance = float(input("Enter the shipping distance in miles: "))
    
    print("Shipping Method Options:")
    print("1. Standard Shipping ($5.00)")
    print("2. Express Shipping ($15.00)")
    
    choice = input("Enter the number of your chosen shipping method (1 for Standard, 2 for Express): ")
    
    if choice == "1":
        shipping_method = "Standard"
    elif choice == "2":
        shipping_method = "Express"
    else:
        print("Invalid choice.")
        return
    shipping_cost = calculate_shipping_cost(weight, distance, shipping_method)
    if shipping_cost is not None:
        print("Shipping cost:", "${:.2f}".format(shipping_cost))

if __name__ == "__main__":
    main()
