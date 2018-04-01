from telegram import InlineQueryResultArticle, InputTextMessageContent
from uuid import uuid4


def inline_query_transform(response_text: str) -> list:
    """
    Formats a response string into a form which can be passed to inline_query.answer()
    """

    return [
        InlineQueryResultArticle(
            id=uuid4(),
            title="_query_result_stg",
            input_message_content=InputTextMessageContent(response_text)
        )
    ]
