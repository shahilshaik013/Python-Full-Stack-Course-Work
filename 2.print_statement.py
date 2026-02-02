# Product details program

product_name = input("Enter the product name: ")
stock = int(input("Enter the stock: "))
price = float(input("Enter the price: "))

ram = input("Enter the available RAM sizes: ")
reviews = input("Enter the reviews: ")
payment_mode = input("Enter the payment modes: ")
brand = input("Enter the brand details: ")

print("\n--- Product Details ---")
print(f"Product Name: {product_name}")
print(f"Stock: {stock}")
print(f"Price: {price}")
print(f"RAM Options: {ram}")
print(f"Reviews: {reviews}")
print(f"Payment Modes: {payment_mode}")
print(f"Brand Details: {brand}")
