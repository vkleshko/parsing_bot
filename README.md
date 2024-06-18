#  Bot for getting vacancy static today 

## Installing using GitHub
Clone the project

```bash
  git clone https://github.com/vkleshko/parsing_bot.git
```

Install dependencies

```bash
  pip install -r requirements.txt
```

### To get your telegram bot token

Creating a new bot in Telegram:
- Open Telegram and search for a bot called @BotFather.
- Press '/start' to start communicating with BotFather.
- Type '/newbot' to create a new bot.
- Enter a name for your bot (eg MyVacancyBot) and press Enter.
- Enter a username for your bot. This should end with bot, for example my_vacancy_bot.

Obtaining a bot token:
- After successfully creating your bot, BotFather will send you a message with the access token for your bot.
- The token will look something like this: '1234567890:ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'.
- Copy this token. And do setuping environment variables.

### Set up environment variables:
```
  set TG_BOT_TOKEN=<your telegram bot token>
```

## Running the Project

To start both the parser and the Telegram bot:

```bash
  python main.py
```
