from dataclasses import dataclass


@dataclass
class Trade:
    direction: str
    entry_time: str
    r_result: int

    def to_dict(self) -> dict:
            return {
                "direction": self.direction,
                "entry_time": self.entry_time,
                "r_result": self.r_result
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Trade":
        return cls(
            direction=data["direction"],
            entry_time=data["entry_time"],
            r_result=data["r_result"]
    )
