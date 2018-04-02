from config import CATE_API_ENDPOINT
from logger import log
from requests import get


def generate_cate_response(query_text: str) -> str:
    """
    Generates a fixed-width version of the query_text. Returns a string;
    must be passed into helpers.inline_query_transform before being used.
    """

    # Save locations of stuff like emoji for later.
    # We're gonna put it back after the API mangles it.
    special_char_locations = _index_special_chars(query_text)

    try:
        result = get("{api_base_url}/{query}".format(
            api_base_url=CATE_API_ENDPOINT, query=query_text
        )).content.decode("utf-8")

        # Now put the special characters back
        if special_char_locations:
            result = list(result)

            for index, char in special_char_locations.items():
                result[index] = char

            result = ''.join(result)
    except Exception as e:
        result = "Error generatin' response, dood! {error}".format(
            error=str(e)
        )

        log.error(e)

    return result

def _index_special_chars(query_text: str) -> dict:
    """
    Given a query string with mixed characters, returns a
    mapping of string index to character.
    """

    # Definition of "special character" is anything
    # outside the BASIC LATIN Unicode range (> 0x007F).
    outside_of_range = lambda char: ord(char) > 127
    result_map = {}
    
    for index in range(len(query_text)):
        if outside_of_range(query_text[index]):
            result_map[index] = query_text[index]

    return result_map

