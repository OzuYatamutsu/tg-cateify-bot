from config import CATE_API_ENDPOINT
from logger import log
from requests import get


def generate_cate_response(query_text: str) -> str:
    """
    Generates a fixed-width version of the query_text. Returns a string;
    must be passed into helpers.inline_query_transform before being used.
    """

    try:
        result = get("{api_base_url}/{query}".format(
            api_base_url=CATE_API_ENDPOINT, query=query_text
        )).content.decode("utf-8")
    except Exception as e:
        result = "Error generatin' response, dood! {error}".format(
            error=str(e)
        )

        log.error(e)

    return result
