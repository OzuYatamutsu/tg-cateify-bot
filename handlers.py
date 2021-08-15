from logger import log_cateify, log_command
from helpers import inline_query_transform, get_meta_from_update
from response_controller import generate_cate_response
from telegram import ParseMode, ChatAction


@log_cateify
def on_inline_query(update, context) -> None:
    """
    Forward the query to the controller method and respond
    """

    username, user_id, query_text = get_meta_from_update(update)

    if not query_text:
        update.inline_query.answer(inline_query_transform(''))
        return

    update.inline_query.answer(inline_query_transform(
        generate_cate_response(query_text=query_text)
    ))


@log_cateify
def on_message_text(update, context) -> None:
    """
    Forward the message text to the controller method and respond
    """

    username, user_id, message_text = get_meta_from_update(update)
    bot = context.bot

    if not message_text:
        return

    bot.send_chat_action(user_id, ChatAction.TYPING)

    bot.sendMessage(
        chat_id=user_id,
        parse_mode=ParseMode.MARKDOWN,
        text=generate_cate_response(query_text=message_text)
    )


@log_command
def on_command_start(update, context):
    """
    Welcomes the user to Cateify bot!
    """

    WELCOME_STICKER_ID = "CAADAQADBQADw8wxE34vqjVrXNMoAg"
    WELCOME_MESSAGE_TEXT = (
        "Ｈｅｗｗｏ！！ (=ↀωↀ=)✧ ；；"
        "\nＷｅｌｃｏｍｅ ｔｏ Ｊｉｎｈａｉ\'ｓ Ｃａｔｅｉｆｙ Ｂｏｔ"
        "\n\nＦｏｒ ｍｏｒｅ ｉｎｆｏ, ｔｒｙ: /help"
    )

    username, user_id, message_text = get_meta_from_update(update)
    bot = context.bot

    bot.send_chat_action(user_id, ChatAction.TYPING)
    bot.sendSticker(
        chat_id=user_id, sticker=WELCOME_STICKER_ID, disable_notification=True
    )
    bot.sendMessage(
        chat_id=user_id, parse_mode=ParseMode.MARKDOWN,
        text=WELCOME_MESSAGE_TEXT
    )


@log_command
def on_command_help(update, context):
    """
    Provides the user with information about the bot.
    """

    HELP_COMMAND_TEXT = (
        "Ｔｏ ｕｓｅ ｉｎｗｉｎｅ ｑｗｕｅｒｉｅｓ，ｐｗｅａｓｅ ｕｓｅ ｔｈｅ ｆｏｗｗｏｗｉｎｇ ｆｏｒｍａｔ:"   # noqa
        "\n`@cateify_bot your message text here`"
        "\nｔｈｅｎ ｓｅｗｅｃｔ ｙｏｕｒ ｏｐｔｉｏｎ ｆｗｏｍ ｔｈｅ ｄｗｏｐｄｏｗｎ ｍｅｎｕ！！ o3o;;"
        "\n\nＹｏｕ ｃａｎ ａｌｓｏ ｊｕｓｔ ｐｗｉｖａｔｅｗｙ ｍｅｓｓａｇｅ ｍｅ， ｏｒ ｒｅｐｗｙ ｔｏ ｍｅ ｉｎ ｇｗｏｕｐ ｃｈａｔｓ,"  # noqa
        "\nａｎｄ Ｉｌｌ ｃａｔｅｉｆｙ ｙｏｕｒ ｍｅｓｓａｇｅｓ！！！₍˄·͈༝·͈˄₎ "
    )

    username, user_id, message_text = get_meta_from_update(update)
    bot = context.bot

    bot.send_chat_action(user_id, ChatAction.TYPING)
    bot.sendMessage(
        chat_id=user_id, parse_mode=ParseMode.MARKDOWN,
        text=HELP_COMMAND_TEXT
    )
