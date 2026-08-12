import csv

def main():
    with open("trades.csv", "w") as file:
        fieldnames = ["Symbol", "Entry", "Exit", "Risk"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow({
    "Symbol": "BTCUSDT",
    "Entry": "76500",
    "Exit": "77000",
    "Risk": "10"
})

    with open("trades.csv", "a") as file:
        fieldnames = ["Symbol", "Entry", "Exit", "Risk"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writerow({
    "Symbol": "ETHUSDT",
    "Entry": "4500",
    "Exit": "4600",
    "Risk": "10"
})

    with open("trades.csv", "r") as file:
        fieldnames = ["Symbol", "Entry", "Exit", "Risk"]
        reader = csv.DictReader(file)
        for row in reader:
            print(f"Symbol: {row["Symbol"]}")
            print(f"Entry: {float(row["Entry"])}")
            print(f"Exit: {float(row["Exit"])}")
            print(f"Risk: {float(row["Risk"])}")


if __name__ == "__main__":
    main()