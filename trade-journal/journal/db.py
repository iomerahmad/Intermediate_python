import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from urllib.parse import quote_plus


load_dotenv()

password = os.getenv("DB_PASSWORD")
encoded_password = quote_plus(password)

DATABASE_URL = f"postgresql+psycopg2://postgres:{encoded_password}@localhost:5432/trade_journal"

engine = create_engine(DATABASE_URL)

if __name__ == "__main__":
    with engine.connect() as connection:
        print("connection established successfully!")