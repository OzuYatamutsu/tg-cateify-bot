from logger import log
from telegram.ext import Updater, InlineQueryHandler, MessageHandler, CommandHandler, Filters
from telegram import ParseMode, ChatAction
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

    log_cateify(username=query_username, user_id=query_user_id, text=query_text)

    update.inline_query.answer(inline_query_transform(
        generate_cate_response(query_text=update.inline_query.query)
    ))

def on_message_text(bot, update) -> None:
    """
    Forward the message text to the controller method and respond
    """

    message_username: str = update.effective_user.username
    message_user_id = str(update.effective_user.id)
    message_text: str = update.message.text

    if not message_text:
        return

    log_cateify(username=message_username, user_id=message_user_id, text=message_text)

    bot.send_chat_action(message_user_id, ChatAction.TYPING)
    generate_cate_response(update.message)

    bot.sendMessage(chat_id=message_user_id, parse_mode=ParseMode.MARKDOWN,
                    text=generate_cate_response(query_text=message_text))


def log_cateify(username, user_id, text):
    """
    Logs important cateification info
    """
    log.debug('Cateifying: "{text}" from user {username} ({id})'.format(
        text=text, username=username, id=user_id
    ))

def on_command_start(bot, update):
    """
    Welcomes the user to Cateify Bot
    """

    message_username: str = update.effective_user.username
    message_user_id = str(update.effective_user.id)
    message_text: str = update.message.text

    log_command(username=message_username, user_id=message_user_id, command=message_text)

    bot.send_chat_action(message_user_id, ChatAction.TYPING)

    bot.sendSticker(chat_id=message_user_id, sticker="CAADAQADBQADw8wxE34vqjVrXNMoAg", disable_notification=True)
    bot.sendMessage(chat_id=message_user_id, parse_mode=ParseMode.MARKDOWN,
                    text='Ｈｅｗｗｏ！！ (=ↀωↀ=)✧ ；；'
                    '\nＷｅｌｃｏｍｅ ｔｏ Ｊｉｎｈａｉ\'ｓ Ｃａｔｅｉｆｙ Ｂｏｔ'
                    '\n\nＦｏｒ ｍｏｒｅ ｉｎｆｏ, ｔｒｙ: /help'
                    )

def on_command_help(bot, update):
    """
    Provides the user with information about the bot
    """
    message_username: str = update.effective_user.username
    message_user_id = str(update.effective_user.id)
    message_text: str = update.message.text

    log_command(username=message_username, user_id=message_user_id, command=message_text)

    bot.send_chat_action(message_user_id, ChatAction.TYPING)

    bot.sendMessage(chat_id=message_user_id, parse_mode=ParseMode.MARKDOWN,
                    text='Ｔｏ ｕｓｅ ｉｎｗｉｎｅ ｑｗｕｅｒｉｅｓ， ｐｗｅａｓｅ ｕｓｅ ｔｈｅ ｆｏｗｗｏｗｉｎｇ ｆｏｒｍａｔ:'
                    '\n＠ｃａｔｅｉｆｙ＿ｂｏｔ ｙｏｕｒｍｅｓｓａｇｅｔｅｘｔｈｅｒｅ'
                    '\nｔｈｅｎ ｓｅｗｅｃｔ ｙｏｕｒ ｏｐｔｉｏｎ ｆｗｏｍ ｔｈｅ ｄｗｏｐｄｏｗｎ ｍｅｎｕ！！ o3o;;'
                    '\n\nＹｏｕ ｃａｎ ａｌｓｏ ｊｕｓｔ ｐｗｉｖａｔｅｗｙ ｍｅｓｓａｇｅ ｍｅ， ｏｒ ｒｅｐｗｙ ｔｏ ｍｅ ｉｎ ｇｗｏｕｐ ｃｈａｔｓ,'
                    '\nａｎｄ Ｉｌｌ ｃａｔｅｉｆｙ ｙｏｕｒ ｍｅｓｓａｇｅｓ！！！₍˄·͈༝·͈˄₎ '
                    )

def log_command(username, user_id, command):
    """
    Logs command usage
    """
    log.debug('Command Detected: "{command}" from user {username} ({id})'.format(
        command=command, username=username, id=user_id
    ))


def start():
    """Connects to Telegram and starts the bot."""

    bot = Updater(token=API_KEY)
    dp = bot.dispatcher

    # Register inline query handler
    dp.add_handler(InlineQueryHandler(on_inline_query))

    # Register command handlers
    dp.add_handler(CommandHandler("start", on_command_start))
    dp.add_handler(CommandHandler("help", on_command_help))

    # Register text message handler
    dp.add_handler(MessageHandler(Filters.text, on_message_text))

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
