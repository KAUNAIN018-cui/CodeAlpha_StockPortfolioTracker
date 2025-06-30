stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 2750,
    "AMZN": 3400
}

portfolio = {}
total = 0

n = int(input("How many stocks do you want to enter? "))
for _ in range(n):
    name = input("Enter stock symbol (e.g., AAPL): ").upper()
    quantity = int(input("Enter quantity: "))
    if name in stock_prices:
        portfolio[name] = quantity
        total += stock_prices[name] * quantity
    else:
        print(f"Stock {name} not found in price list.")

print("\nYour Portfolio:")
for stock, qty in portfolio.items():
    print(f"{stock} - {qty} shares @ ${stock_prices[stock]} = ${qty * stock_prices[stock]}")

print(f"Total Investment Value: ${total}")

# Save to file (optional)
with open("portfolio_result.txt", "w") as file:
    for stock, qty in portfolio.items():
        file.write(f"{stock},{qty},{stock_prices[stock]},{qty * stock_prices[stock]}\n")
    file.write(f"Total, , ,${total}\n")
