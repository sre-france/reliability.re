import os
import re
import sys
import json
from html import unescape
from unicodedata import normalize

import twitter
from twitter.twitter_utils import calc_expected_status_length, is_url
from twitter.api import CHARACTER_LIMIT


CONSUMER_KEY = os.environ.get("TWITTER_CONSUMER_KEY")
CONSUMER_SECRET = os.environ.get("TWITTER_CONSUMER_SECRET")
ACCESS_TOKEN_KEY = os.environ.get("TWITTER_ACCESS_TOKEN_KEY")
ACCESS_TOKEN_SECRET = os.environ.get("TWITTER_ACCESS_TOKEN_SECRET")

SHORT_URL_LENGTH = 23


def word_length(word):
    """
    Calculate the length of a word on Twitter.

    It takes into account the size of shortened URLs and
    unicode emojis.
    See https://developer.twitter.com/en/docs/counting-characters
    """
    unicode_ranges = [
        range(0, 4351),
        range(8192, 8205),
        range(8208, 8223),
        range(8242, 8247),
    ]
    length = 0
    if is_url(word):
        length = SHORT_URL_LENGTH
    else:
        for char in word:
            if any(
                [
                    ord(normalize("NFC", char)) in char_range
                    for char_range in unicode_ranges
                ]
            ):
                length += 1
            else:
                length += 2
    return length


def format_tweets(payload):
    """
    Split plain text content into a list.

    The length of every element can't be higher than CHARACTER_LIMIT (280 characters).

    The formatting rules defined here are:

    1. The first element (even if there's only one) must include its attribution (link and author) at the end.
       It must be at the end because Twitter only generated a card preview for the last link in a tweet.
    2. If there's more than 1 tweet, all the tweets include a placeholder ([…]) to indicate the continuation,
       except the last one.

    For more examples take a look at the test suite.
    """
    content = payload["plain"]
    content = " ".join(content.split())
    content = unescape(content)
    ending = """ {link} shared by @{username}""".format(
        link=payload["link"], username=payload["twitter_username"]
    )

    placeholder = " […]"
    current_line_length = 0
    line = []
    tweets = []
    words = re.split(r"\s", content)

    for word in words:
        current_line_length += word_length(word) + 1

        if len(tweets) == 0:
            if current_line_length > (
                CHARACTER_LIMIT - calc_expected_status_length(placeholder + ending)
            ):
                tweets.append(" ".join(line) + placeholder + ending)
                line = [word]
                current_line_length = word_length(word)
            else:
                line.append(word)
        else:
            if current_line_length > (
                CHARACTER_LIMIT - calc_expected_status_length(placeholder)
            ):
                tweets.append(" ".join(line) + placeholder)
                line = [word]
                current_line_length = word_length(word)
            else:
                line.append(word)
    if len(tweets) == 0:
        tweets.append(" ".join(line) + ending)
    else:
        tweets.append(" ".join(line))
    return tweets


def send_tweets(tweets):
    """
    Publish tweets as a thread.
    """
    total = len(tweets)
    for i, tweet in enumerate(tweets):
        length = calc_expected_status_length(tweet)
        nro = i + 1
        print(
            "Tweet {nro}/{total} ({length} chars):\n{tweet}".format(
                nro=nro, total=total, length=length, tweet=tweet
            )
        )

    api = twitter.Api(
        consumer_key=CONSUMER_KEY,
        consumer_secret=CONSUMER_SECRET,
        access_token_key=ACCESS_TOKEN_KEY,
        access_token_secret=ACCESS_TOKEN_SECRET,
    )
    last_reply_to_id = None
    for tweet in tweets:
        status = api.PostUpdate(tweet, in_reply_to_status_id=last_reply_to_id)
        last_reply_to_id = status.id
    return


def main(filename):
    with open(filename, "r") as f:
        payload = json.load(f)
    tweets = format_tweets(payload)
    send_tweets(tweets)


if __name__ == "__main__":
    filename = sys.argv[1]
    main(filename)
