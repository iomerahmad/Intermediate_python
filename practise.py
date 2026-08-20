from pathlib import Path

data_dir = Path("data")
logs_dir = Path("logs")

data_dir.mkdir(exist_ok=True)
logs_dir.mkdir(exist_ok=True)

trades_file = Path("data") / "traders.csv"
trades_file.touch(exist_ok=True)

if trades_file.exists():
    print("File found")
else:
    print("File does not exist yet")