from logger import log
from telegram.ext import Updater, InlineQueryHandler
from response_controller import generate_cate_response
from config import API_KEY
from helpers import inline_query_transform


def on_inline_query(bot, update) -> None:
    """
    Forward the query to the controller method and respond
    """

    query_username: str = update.effective_user.username
    query_user_id = str(update.effective_user.id)
    query_text: str = update.inline_query.query

    if not query_text:
        update.inline_query.answer(inline_query_transform(''))
        return

    log.debug('Cateifying: "{text}" from user {username} ({id})'.format(
        text=query_text, username=query_username, id=query_user_id
    ))

    update.inline_query.answer(inline_query_transform(
        generate_cate_response(query_text=update.inline_query.query)
    ))


def start():
    """Connects to Telegram and starts the bot."""

    bot = Updater(token=API_KEY)
    dp = bot.dispatcher

    # Register inline query handler
    dp.add_handler(InlineQueryHandler(on_inline_query))

    log.info("Bot ready, dood! Connected as {username} (with ID {id}).".format(
        username=bot.bot.username,
        id=bot.bot.id
    ))
    bot.start_polling()
    bot.idle()


def _onboard_config():
    global API_KEY

    with open('config.py', 'r') as f:
        config_contents = f.read()

    print("Hiya. Looks like you're startin' cateify-bot for the first time.")
    bot_token: str = input("What's your bot token? ")

    with open('config.py', 'w') as f:
        f.write(config_contents.format(api_key=bot_token))

    API_KEY = bot_token
    print("Done!")


if __name__ == '__main__':
    if API_KEY == '{api_key}':
        _onboard_config()
    start()
