# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 2700,
    "MSFT": 320,
    "AMZN": 140
}

portfolio = {}
total_investment = 0

print("Stock Portfolio Tracker")

# Number of stocks user wants to enter
n = int(input("Enter number of different stocks: "))

for i in range(n):
    stock = input("Enter stock name (AAPL, TSLA, GOOG, MSFT, AMZN): ").upper()
    quantity = int(input("Enter quantity: "))
    
    if stock in stock_prices:
        portfolio[stock] = quantity
    else:
        print("Stock not available.")

# Calculate total investment
for stock, quantity in portfolio.items():
    price = stock_prices[stock]
    investment = price * quantity
    total_investment += investment
    print(stock, ":", quantity, "shares x", price, "=", investment)

print("\nTotal Investment Value =", total_investment)

# Optional: Save result to file
save = input("Do you want to save the result to file? (yes/no): ")

if save.lower() == "yes":
    file = open("portfolio.txt", "w")
    file.write("Stock Portfolio\n")
    
    for stock, quantity in portfolio.items():
        price = stock_prices[stock]
        investment = price * quantity
        file.write(f"{stock}: {quantity} shares x {price} = {investment}\n")
    
    file.write(f"\nTotal Investment Value = {total_investment}")
    file.close()
    
    print("Portfolio saved to portfolio.txt")