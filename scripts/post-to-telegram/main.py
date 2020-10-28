#!/usr/bin/env python3
import sys
import json
import os
from html import unescape

import telegram
from feedparser.sanitizer import _HTMLSanitizer


TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")

TEMPLATE = """
<em>From</em> {link}

{content}

<em>Shared by {user} via reliability.re</em>
"""


def clean_html(content):
    p = _HTMLSanitizer(None, "text/html")
    p.acceptable_elements = {
        "b",
        "strong",
        "i",
        "em",
        "underline",
        "ins",
        "s",
        "strike",
        "del",
        "a",
        "code",
        "pre",
    }
    p.acceptable_attributes = {"href"}
    p.feed(content)
    cleaned = p.output()
    cleaned = cleaned.strip()
    cleaned = unescape(cleaned)
    return cleaned


def format_message(payload):
    """
    Format HTML content on a subset of HTML tags supported by the Telegram Bot API.
    See https://core.telegram.org/bots/api#html-style
    """

    user = '<a href="https://github.com/{username}">@{username}</a>'.format(
        username=payload["github_username"]
    )
    content = clean_html(payload["content"])
    message = TEMPLATE.format(
        link=payload["link"],
        content=content,
        user=user,
    )
    return message.strip()


def send_message(message):
    bot = telegram.Bot(token=TELEGRAM_TOKEN)
    chat_id = TELEGRAM_CHAT_ID
    bot.sendMessage(
        chat_id=chat_id,
        text=message,
        disable_web_page_preview=False,
        parse_mode=telegram.ParseMode.HTML,
    )


def main(filename):
    with open(filename, "r") as f:
        payload = json.load(f)
    message = format_message(payload)
    send_message(message)


if __name__ == "__main__":
    filename = sys.argv[1]
    main(filename)
