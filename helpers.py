from telegram import InlineQueryResultArticle, InputTextMessageContent
from uuid import uuid4


def inline_query_transform(response_text: str, title=None) -> list:
    """
    Formats a response string into a form which can be passed
    to inline_query.answer(). If the title isn't passed, will
    just use the response text as the title, too.
    """

    return [
        InlineQueryResultArticle(
            id=uuid4(),
            title=title if title else response_text,
            input_message_content=InputTextMessageContent(response_text)
        )
    ]
