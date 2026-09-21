from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from datetime import datetime

class Base(DeclarativeBase):
    pass

class TradeORM(Base):
    __tablename__ = "trades"

    id: Mapped[int] = mapped_column(primary_key=True)
    direction: Mapped[str]
    entry_time: Mapped[datetime]
    r_result: Mapped[float]
    
