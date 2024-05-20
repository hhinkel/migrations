from sqlalchemy import create_engine
from sqlalchemy.sql import text

engine = create_engine("postgresql+psycopg2://postgres:Arthur@0.0.0.0:5432/mydb")

def app():
    with engine.connect() as conn:
        stmt = text("select * from pg_database")
        print(conn.execute(stmt).fetchall())


if __name__ == "__main__":
    app()