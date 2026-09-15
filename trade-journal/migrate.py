import json
from journal.database import add_trade
from journal.trade import Trade

def main():
    with open("trades.json") as f:
        trade_list = json.load(f)
        counter = 0
        for trade in trade_list:
            direction = trade["direction"]
            direction = direction.lower()
            entry_time=trade["entry_time"]
            r_result=trade["r_result"]
            final_trade = Trade(direction=direction, entry_time=entry_time, r_result=r_result)
            add_trade(final_trade)
            counter += 1
        print(counter)


if __name__ == "__main__":
    main()
