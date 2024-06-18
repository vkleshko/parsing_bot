import os
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import FSInputFile, Message
from dotenv import load_dotenv

from app.reporting import create_excel_report

load_dotenv()

bot = Bot(token=os.environ["TG_BOT_TOKEN"])
dp = Dispatcher()


async def send_excel_report(chat_id: int) -> None:
    """Creates an Excel report and sends it to the specified Telegram chat."""

    create_excel_report()
    report_file = FSInputFile("report.xlsx")
    await bot.send_document(chat_id, report_file)


@dp.message(Command("get_today_statistic"))
async def get_today_statistic(message: Message) -> None:
    """Handles the /get_today_statistic command. Sends today's statistics as an Excel report."""

    chat_id = message.chat.id
    await send_excel_report(chat_id)


async def polling():
    """Starts the bot's polling mechanism to listen for incoming messages."""

    await dp.start_polling(bot)
