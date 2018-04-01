from config import CATE_API_ENDPOINT
from helpers import inline_query_transform
from requests import get


def generate_cate_response(query_text: str) -> list:
    """
    Generates a fixed-width version of the query_text.
    Returns a properly formatted inline query response.
    """

    try:
        result = get("{api_base_url}/{query}".format(
            api_base_url=CATE_API_ENDPOINT, query=query_text
        )).content
    except Exception as e:
        result = "Error generatin' response, dood! {error}".format(
            error=str(e)
        )

    return inline_query_transform(result)
