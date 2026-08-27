class TradeJournal:
    def __init__(self, trades=[]):
        self.trades = trades
        self.starting_balance = 1000

    def add_trade(self, symbol, pnl):
        trade = {"symbol": symbol, "pnl": pnl}
        self.trades.append(trade)

    def win_rate(self):
        wins = 0
        for trade in self.trades:
            if trade["pnl"] > 0:
                wins += 1
        return wins / len(self.trades) * 100

    def total_pnl(self):
        total = 0
        for trade in self.trades:
            total = total + trade["pnl"]
        return total

    @classmethod
    def from_dict(data):
        journal = TradeJournal()
        journal.trades = data["trades"]
        return journal



j1 = TradeJournal()
j1.add_trade("BTC", 50)

j2 = TradeJournal()
print(j2.trades)