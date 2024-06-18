import asyncio
import schedule
import requests
from urllib.parse import urljoin

from app.database import create

BASE_URL = "https://ua-api.robota.ua/"
JUNIOR_URL = urljoin(BASE_URL, "vacancy/search?keyWords=junior")


def get_vacancy_count() -> int:
    """Extract the vacancy count from the API."""

    response = requests.get(JUNIOR_URL)
    if response.status_code == 200:
        json_data = response.json()
        vacancy_count = json_data["total"]
        return vacancy_count
    return 0


def create_new_record() -> None:
    """Creates a new record with the current time and vacancy count."""

    vacancy_count = get_vacancy_count()
    create(vacancy_count=vacancy_count)


async def schedule_parsing() -> None:
    """Schedules the creation of new records every hour."""

    schedule.every(1).hours.do(create_new_record)
    while True:
        schedule.run_pending()
        await asyncio.sleep(1)
