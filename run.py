from config import API_KEY
from telegram.ext import Updater, InlineQueryHandler
from response_controller import generate_cate_response
from logger import log


def on_inline_query(bot, update) -> None:
    # Forward the query to the controller method and respond
    update.inline_query.answer(
        generate_cate_response(query_text=update.inline_query.query)
    )


def start():
    """Connects to Telegram and starts the bot."""

    bot = Updater(token=API_KEY)
    dp = bot.dispatcher
    dp.add_handler(InlineQueryHandler(on_inline_query))
    log.info("Bot ready, dood!")
    bot.start_polling()
    bot.idle()


if __name__ == '__main__':
    start()


