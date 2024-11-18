import pandas as pd

class StockPortfolio:
    def __init__(self):
        self.stocks = {}

    def add_stock(self):
        stock_name = input("Enter the name of the stock: ")
        stock_symbol = input(f"Enter the symbol for {stock_name}: ")
        self.stocks[stock_symbol] = {
            'name': stock_name,
            'prices': {'buy': None, 'sell': None},
            'exposure': {'shares_owned': None, 'risk_factor': None}
        }
        print(f"{stock_name} ({stock_symbol}) added to portfolio.")

    def update_prices(self):
        symbol = input("Enter the symbol of the stock to update prices: ")
        if symbol in self.stocks:
            buy_price = float(input(f"Current buying price of {symbol}: "))
            sell_price = float(input(f"Current selling price of {symbol}: "))
            self.stocks[symbol]['prices']['buy'] = buy_price
            self.stocks[symbol]['prices']['sell'] = sell_price
            print(f"Prices updated for {self.stocks[symbol]['name']} ({symbol}).")
        else:
            print("Stock not found in portfolio.")

    def update_exposure(self):
        symbol = input("Enter the symbol of the stock to update exposure: ")
        if symbol in self.stocks:
            shares_owned = float(input(f"Current number of {symbol} stocks owned: "))
            risk_factor = float(input(f"Current risk factor of {symbol} share ownership: "))
            self.stocks[symbol]['exposure']['shares_owned'] = shares_owned
            self.stocks[symbol]['exposure']['risk_factor'] = risk_factor
            print(f"Exposure updated for {self.stocks[symbol]['name']} ({symbol}).")
        else:
            print("Stock not found in portfolio.")

    def calculate_highest_profit(self):
        highest_profit = 0
        highest_stock_name = ''
        for symbol, details in self.stocks.items():
            if all(details['prices'].values()) and all(details['exposure'].values()):
                buy_price = details['prices']['buy']
                sell_price = details['prices']['sell']
                shares_owned = details['exposure']['shares_owned']
                risk_factor = details['exposure']['risk_factor']
                
                total_profit = ((sell_price - buy_price) - (risk_factor * buy_price)) * shares_owned
                if total_profit > highest_profit:
                    highest_profit = total_profit
                    highest_stock_name = details['name']

        if highest_stock_name:
            print(f"Highest selling stock is {highest_stock_name} with a profit margin of {highest_profit}.")
        else:
            print("Portfolio does not have sufficient data for profit calculation.")

def main():
    portfolio = StockPortfolio()

    while True:
        print("\nMenu")
        print("1: Add a stock")
        print("2: Update stock prices")
        print("3: Update exposure")
        print("4: Find the highest sale price")
        print("5: Exit")

        user_choice = input("Enter your choice (1-5): ")

        if user_choice == '1':
            portfolio.add_stock()
        elif user_choice == '2':
            portfolio.update_prices()
        elif user_choice == '3':
            portfolio.update_exposure()
        elif user_choice == '4':
            portfolio.calculate_highest_profit()
        elif user_choice == '5':
            print("Ending stock program.")
            break
        else:
            print("Invalid choice. Please enter a valid option (1-5).")

if __name__ == "__main__":
    main()
