import pytest
from datetime import datetime
from journal.trade import Trade
from journal.database import add_trade, get_all_trades
from journal.models import Journal
from journal.db import engine
from journal.orm_models import TradeORM
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError


@pytest.fixture
def clean_db():
    """Wipes the trades table before and after each test, so tests don't
    interfere with each other or your real data."""
    with Session(engine) as session:
        session.query(TradeORM).delete()
        session.commit()
    yield
    with Session(engine) as session:
        session.query(TradeORM).delete()
        session.commit()


# --- Trade dataclass ---

def test_trade_to_dict():
    trade = Trade(direction="long", entry_time="2026-09-19 20:00", r_result=1.5)
    assert trade.to_dict() == {
        "direction": "long",
        "entry_time": "2026-09-19 20:00",
        "r_result": 1.5,
    }

def test_trade_from_dict():
    data = {"direction": "short", "entry_time": "2026-09-20 10:00", "r_result": -1.0}
    trade = Trade.from_dict(data)
    assert trade.direction == "short"
    assert trade.entry_time == "2026-09-20 10:00"
    assert trade.r_result == -1.0

def test_trade_round_trip():
    original = Trade(direction="long", entry_time="2026-09-19 20:00", r_result=2.0)
    rebuilt = Trade.from_dict(original.to_dict())
    assert original == rebuilt


# --- database.py (ORM layer) ---

def test_add_and_get_single_trade(clean_db):
    trade = Trade(direction="long", entry_time=datetime(2026, 9, 19, 20, 0), r_result=1.5)
    add_trade(trade)
    trades = get_all_trades()
    assert len(trades) == 1
    assert trades[0].direction == "long"
    assert trades[0].r_result == 1.5

def test_add_multiple_trades(clean_db):
    add_trade(Trade(direction="long", entry_time=datetime(2026, 9, 19, 20, 0), r_result=1.0))
    add_trade(Trade(direction="short", entry_time=datetime(2026, 9, 20, 10, 0), r_result=-0.5))
    trades = get_all_trades()
    assert len(trades) == 2

def test_get_all_trades_empty(clean_db):
    trades = get_all_trades()
    assert trades == []

def test_invalid_direction_rejected(clean_db):
    with pytest.raises(IntegrityError):
        with Session(engine) as session:
            bad = TradeORM(direction="medium", entry_time=datetime(2026, 9, 20, 10, 0), r_result=1.0)
            session.add(bad)
            session.commit()

def test_entry_time_stored_as_datetime(clean_db):
    trade = Trade(direction="long", entry_time=datetime(2026, 9, 19, 20, 0), r_result=1.5)
    add_trade(trade)
    trades = get_all_trades()
    assert isinstance(trades[0].entry_time, datetime)


# --- Journal (business logic layer) ---

def test_journal_add_trade_rejects_wrong_type():
    journal = Journal()
    with pytest.raises(TypeError):
        journal.add_trade("not a trade")

def test_journal_win_rate_no_trades(clean_db):
    journal = Journal()
    assert journal.win_rate() == 0.0

def test_journal_win_rate_calculation(clean_db):
    add_trade(Trade(direction="long", entry_time=datetime(2026, 9, 19, 20, 0), r_result=1.0))
    add_trade(Trade(direction="short", entry_time=datetime(2026, 9, 20, 10, 0), r_result=-1.0))
    journal = Journal()
    assert journal.win_rate() == 50.0

def test_journal_expectancy_no_trades(clean_db):
    journal = Journal()
    assert journal.expectancy() == 0.0

def test_journal_expectancy_calculation(clean_db):
    add_trade(Trade(direction="long", entry_time=datetime(2026, 9, 19, 20, 0), r_result=2.0))
    add_trade(Trade(direction="short", entry_time=datetime(2026, 9, 20, 10, 0), r_result=-1.0))
    journal = Journal()
    assert journal.expectancy() == 0.5