from logger import log
from telegram.ext import Updater, InlineQueryHandler, MessageHandler, CommandHandler, Filters
from telegram import ParseMode, ChatAction
from helpers import inline_query_transform
from response_controller import generate_cate_response


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

