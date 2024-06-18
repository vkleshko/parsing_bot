import asyncio
from app.parse import schedule_parsing
from bot.telegram_bot import polling


async def main() -> None:
    parser_task = asyncio.create_task(schedule_parsing())
    bot_task = asyncio.create_task(polling())
    await asyncio.gather(parser_task, bot_task)


if __name__ == "__main__":
    asyncio.run(main())
