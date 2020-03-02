import re
from importlib import import_module


def completion(match: re.Match) -> str:
    """
    same function from textfsm.clitable
    """

    word = str(match.group())[2:-2]  # strips the double square
    return "(" + ("(").join(word) + ")?" * len(word)


def net_parse(device_type: str, command: str, data: str) -> dict:
    vendor, os = device_type.split("_")
    for key, func in import_module(f"parsefy.network.{vendor}.{os}").MAPPER.items():
        if re.search(re.sub(r"(\[\[.+?\]\])", completion, key), command):
            return func(data)
    raise ValueError

