import json

def main():

    trades = [
        {
            "symbol": "BTCUSDT",
            "entry": 60000,
            "exit": 62000,
            "risk": 100
        }
    ]

    with open("trades.json", "w") as file:
        json.dump(trades, file)

    with open("trades.json", "r") as file:
        trades = json.load(file)
        print(trades)

if __name__ == "__main__":
    main()