import json

class Trade:
    def __init__(self, direction: str, entry: float, entry_time: str, r_result: int):
        self.direction = direction
        self.entry = entry
        self.entry_time = entry_time
        self.r_result = r_result

    def to_dict(self) -> dict:
            return {
                "direction": self.direction,
                "entry": self.entry,
                "entry_time": self.entry_time,
                "r_result": self.r_result
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Trade":
        return cls(
            direction=data["direction"],
            entry=data["entry"],
            entry_time=data["entry_time"],
            r_result=data["r_result"]
    )


class Journal:
    def __init__(self):
        self.trades: list[Trade] = []

    def save(self):
        data = [trade.to_dict() for trade in self.trades]
        with open("trades.json", "w") as file:
            json.dump(data, file, indent=4)

    def load(self):
        with open("trades.json") as file:
            trades = json.load(file)
            self.trades = [Trade.from_dict(item) for item in trades]

    def add_trade(self, trade: Trade) -> None:
        if not isinstance(trade, Trade):
            raise TypeError("add_trade expects a Trade object")
        self.trades.append(trade)

    def print_all_trades(self) -> None:
        if not self.trades:
            print("No trades yet.")
            return
        for trade in self.trades:
            print(f"{trade.direction} | entry: {trade.entry} @ {trade.entry_time} | R: {trade.r_result}")

    def win_rate(self) -> float:
        if not self.trades:
            return 0.0
        wins = sum(1 for trade in self.trades if trade.r_result > 0)
        return wins / len(self.trades) * 100

    def expectancy(self) -> float:
        if not self.trades:
            return 0.0
        total_r = sum(trade.r_result for trade in self.trades)
        return total_r / len(self.trades)

raw_trades = [
    ("short", "8PM Friday", -1),
    ("Long", "11AM Tuesday", -1),
    ("Long", "2AM Friday", 4),
    ("Long", "7PM Wednesday", 4),
    ("Long", "4:30 Friday", 4),
    ("Long", "10:30 Tuesday", -1),
    ("Long", "11PM Jan 6", 4),
    ("Long", "6:45PM Jan 8", 4),
    ("Long", "5AM 19 Jan", -1),
    ("Long", "8PM 20 Jan", -1),
    ("Long", "8:30 25 Jan", -1),
    ("Long", "00:00 26 Jan", -1),
    ("Long", "20:15 28 Jan", 4),
    ("short", "19:30 30 Jan", -1),
    ("short", "00:45 31 Jan", 4),
    ("short", "20:00 2 Feb", 4),
    ("short", "18:00 6 Feb", -1),
    ("short", "22:00 6 Feb", 4),
    ("short", "04:00 7 Feb", 4),
    ("short", "01:00 25 Feb", -1),
    ("short", "01:15 25 Feb", 4),
    ("short", "17:45 28 Feb", -1),
    ("short", "18:45 28 Feb", -1),
    ("short", "03:00 9 Mar", -1),
    ("short", "5:45 9 Mar", 4),
    ("short", "16:00 23 Mar", -1),
    ("short", "16:00 23 Mar", -1),
    ("short", "12:00 1 Apr", 4),
    ("short", "04:00 8 Apr", -1),
    ("short", "21:00 17 Apr", 4),
    ("Long", "20:15 7 May", -1),
    ("Long", "21:00 13 May", 4),
    ("Long", "15:15 16 May", -1),
    ("Long", "04:00 23 May", -1),
    ("short", "01:30 24 May", -1),
    ("short", "2:30 24 May", -1),
    ("short", "20:00 25 May", 4),
    ("short", "21:00 25 May", 4),
    ("short", "13:30 7 Jun", -1),
    ("short", "03:15 8 Jun", 4),
    ("short", "02:00 14 Jun", -1),
    ("Long", "20:15 18 Jun", -1),
    ("Long", "20:00 18 Jun", 4),
    ("Long", "19:30 24 Jun", -1),
    ("Long", "22:00 24 Jun", -1),
    ("Long", "05:45 28 Jul", -1),
]

j = Journal()
for direction, entry_time, r in raw_trades:
    j.add_trade(Trade(direction=direction, entry=None, entry_time=entry_time, r_result=r))

j.save()
j.print_all_trades()
print("Win rate:", j.win_rate())
print("Expectancy:", j.expectancy())
wins = sum(1 for _, _, r in raw_trades if r == 4)
losses = sum(1 for _, _, r in raw_trades if r == -1)
print(wins, losses, wins + losses)
              
