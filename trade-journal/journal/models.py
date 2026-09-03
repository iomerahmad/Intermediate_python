import json
import logging
from pathlib import Path
from dataclasses import dataclass

BASE_DIR = Path(__file__).parent.parent

logging.basicConfig(
    filename=BASE_DIR / "journal.log",
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(message)s"
)
logger = logging.getLogger(__name__)

@dataclass
class Trade:
    direction: str
    entry: float
    entry_time: str
    r_result: int

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

    def save(self) -> None:
        try:
            data = [trade.to_dict() for trade in self.trades]
            with open(BASE_DIR / "trades.json", "w") as file:
                json.dump(data, file, indent=4)
                logger.debug("Saved %d trades to trades.json", len(self.trades))
        except OSError as e:
            logger.error("Could not save trades: %s", e)
            raise

    def load(self) -> None:
        try:
            with open(BASE_DIR / "trades.json") as file:
                trades = json.load(file)
                self.trades = [Trade.from_dict(item) for item in trades]
                logger.debug("Loaded %d trades from trades.json", len(self.trades))
        except FileNotFoundError:
            logger.info("No trades.json found — starting with empty journal")
            self.trades = []
        except json.JSONDecodeError as e:
            logger.warning("trades.json is corrupted, starting fresh: %s", e)
            self.trades = []

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
