import os
import pandas as pd

from app.database import get_today_records


def calculate_change(vacancies_df: pd.DataFrame) -> pd.DataFrame:
    """Calculates the change in vacancy count compared to the previous record."""

    vacancies_df["change"] = (
        vacancies_df["vacancy_count"].diff().fillna(value=0).astype(int)
    )

    return vacancies_df


def create_excel_report() -> None:
    """Creates an Excel report, overwriting the existing file if it exists."""

    records = get_today_records()
    vacancies_df = calculate_change(records)

    if os.path.exists("report.xlsx"):
        os.remove("report.xlsx")

    with pd.ExcelWriter("report.xlsx", engine="xlsxwriter") as writer:
        vacancies_df.to_excel(writer, sheet_name="Vacancies", index=False)

        worksheet = writer.sheets["Vacancies"]

        worksheet.set_column("A:A", 15)
        worksheet.set_column("B:B", 15)
