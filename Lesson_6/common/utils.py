"""Утилиты"""

import json
from variables import MAX_PACKAGE_LENGTH, ENCODING
from errors import *
from decos import log


@log
def get_message(client):
    """
    Утилита приёма и декодирования сообщенияпринимает байты выдаёт словарь,
    если приняточто-то другое отдаёт ошибку значения
    :param client:
    :return:
    """
    encoded_response = client.recv(MAX_PACKAGE_LENGTH)
    if isinstance(encoded_response, bytes):
        response = json.loads(encoded_response.decode(ENCODING))
        if isinstance(response, dict):
            return response
        raise IncorrectDataReceivedError
    raise IncorrectDataReceivedError


@log
def send_message(sock, message):
    """
    Утилита кодирования и отправки сообщения
    принимает словарь и отправляет его
    :param sock:
    :param message:
    :return:
    """
    if not isinstance(message, dict):
        raise NonDictInputError
    sock.send(json.dumps(message).encode(ENCODING))
