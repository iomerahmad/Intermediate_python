from journal.orm_models import TradeORM
from journal.trade import Trade
from journal.db import engine
from sqlalchemy.orm import Session


def main():
    pass

def get_all_trades() -> list[Trade]:
    with Session(engine) as session:
        trades_orm = session.query(TradeORM).all()
        trades = []
        for trade_orm in trades_orm:
            trade = Trade(
                direction = trade_orm.direction,
                entry_time = trade_orm.entry_time,
                r_result = trade_orm.r_result 
            )
            trades.append(trade)
        return trades

def add_trade(trade: Trade) -> None:
    with Session(engine) as session:
        new = TradeORM(
            direction = trade.direction,
            entry_time = trade.entry_time,
            r_result = trade.r_result 
        )
        session.add(new)
        session.commit()
        

if __name__ == "__main__":
    main()
