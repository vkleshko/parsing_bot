import sqlite3
import pandas as pd
from datetime import datetime as dt


def create_table() -> None:
    """Creates the 'vacancies' table in the SQLite database if it doesn't exist already."""

    sql_statements = [
        """CREATE TABLE IF NOT EXISTS vacancies (
                id INTEGER PRIMARY KEY, 
                datetime datetime NOT NULL, 
                vacancy_count INT NOT NULL
        );"""
    ]

    try:
        with sqlite3.connect("robota.sqlite3") as conn:
            cursor = conn.cursor()
            for statement in sql_statements:
                cursor.execute(statement)
            conn.commit()
    except sqlite3.Error as e:
        print(f"An error occurred while creating the table: {e}")


def create(vacancy_count: int) -> None:
    """Inserts a new record into the 'vacancies' table with the given vacancy_count."""

    create_table()
    current_time = dt.now().strftime("%d.%m.%Y %H:%M")

    try:
        with sqlite3.connect("robota.sqlite3") as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO vacancies (datetime, vacancy_count) VALUES (?, ?)",
                (current_time, vacancy_count),
            )
            conn.commit()
    except sqlite3.Error as e:
        print(f"An error occurred while inserting data: {e}")


def get_today_records() -> pd.DataFrame | None:
    """Retrieves records from the 'vacancies' table for the current day."""

    create_table()

    today = dt.now().strftime("%d.%m.%Y")
    query = (
        f"SELECT datetime, vacancy_count FROM vacancies WHERE datetime LIKE '{today}%'"
    )

    with sqlite3.connect("robota.sqlite3") as conn:
        vacancies_df = pd.read_sql_query(query, conn)

    return vacancies_df
