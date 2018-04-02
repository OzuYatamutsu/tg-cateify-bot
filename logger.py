from logging import getLogger, StreamHandler, FileHandler, DEBUG
from sys import stdout


def log_cateify(username: str, user_id: str, text: str) -> None:
    """
    Logs important cateification info (i.e. when we're calling
    into the response controller).
    """

    log.debug('Cateifying: "{text}" from user {username} ({id})'.format(
        text=text, username=username, id=user_id
    ))


def log_command(username: str, user_id: str, command: str) -> None:
    """
    Logs important COMMANDification info (i.e. when /commands are used).
    """

    log.debug('Command: "{command}" from user {username} ({id})'.format(
        command=command, username=username, id=user_id
    ))


log = getLogger(__name__)
log.setLevel(DEBUG)
log.addHandler(StreamHandler(stdout))
log.addHandler(FileHandler('cateify_bot.log'))
