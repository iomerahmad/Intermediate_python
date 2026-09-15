import logging
from pathlib import Path
from journal import database
from journal.database import get_all_trades
from journal.trade import Trade

BASE_DIR = Path(__file__).parent.parent

logging.basicConfig(
    filename=BASE_DIR / "journal.log",
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(message)s"
)
logger = logging.getLogger(__name__)


class Journal:
    def __init__(self):
        pass

    def add_trade(self, trade: Trade) -> None:
        if not isinstance(trade, Trade):
            raise TypeError("add_trade expects a Trade object")
        database.add_trade(trade)


    def print_all_trades(self) -> None:
        trades = get_all_trades()
        if not trades:
            print("No trades yet.")
            return
        for trade in trades:
            print(f"{trade.direction} | {trade.entry_time} | R: {trade.r_result}")

    def win_rate(self) -> float:
        trades = get_all_trades()
        if not trades:
            return 0.0
        wins = sum(1 for trade in trades if trade.r_result > 0)
        return round(wins / len(trades) * 100, 2)

    def expectancy(self) -> float:
        trades = get_all_trades()
        if not trades:
            return 0.0
        total_r = sum(trade.r_result for trade in trades)
        return round(total_r / len(trades), 2)
