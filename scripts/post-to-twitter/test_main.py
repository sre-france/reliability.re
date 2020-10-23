#!/usr/bin/env python3
import json
import unittest

from main import format_tweets, word_length
from main import SHORT_URL_LENGTH


class TestWordLength(unittest.TestCase):
    def test_a_letter(self):
        word = "a"
        self.assertEqual(word_length(word), 1)

    def test_a_latin_letter(self):
        word = "à"
        self.assertEqual(word_length(word), 1)

    def test_latin_letter_with_circumflex(self):
        word = "Ồ"
        self.assertEqual(word_length(word), 2)

    def test_url(self):
        word = "https://example.com/"
        self.assertEqual(word_length(word), SHORT_URL_LENGTH)

    def test_long_url(self):
        word = "https://developer.twitter.com/en/docs/counting-characters"
        self.assertEqual(word_length(word), SHORT_URL_LENGTH)

    def test_emoji(self):
        word = "👾"
        self.assertEqual(word_length(word), 2)


class TestFormatTweets(unittest.TestCase):
    def test_basic(self):
        """A basic test for the Happy Path."""
        with open("test_data/01-payload.json", "r") as f:
            payload = json.load(f)
        expected = [
            "This is the content. https://www.example.com/an-example/ shared by @pabluk"
        ]

        tweets = format_tweets(payload)
        self.assertEqual(tweets, expected)

    def test_long_text(self):
        """Test a long tweet."""
        with open("test_data/02-payload-long-text.json", "r") as f:
            payload = json.load(f)
        expected = [
            "This succinct article from the Honeycomb blog is a great starting point to understand the fundamentals of "
            "Observability, like metrics, logs, traces and structured events, as well as the concepts of context, "
            "dimensionality and […] https://www.honeycomb.io/blog/observability-101-terminology-and-concepts/ shared "
            "by @pabluk",
            "cardinality. It also includes additional links for further reading about #o11y and distributed tracing.",
        ]

        tweets = format_tweets(payload)
        self.assertEqual(tweets, expected)

    def test_very_long_text(self):
        """Test a very long tweet."""
        with open("test_data/03-payload-very-long-text.json", "r") as f:
            payload = json.load(f)
        expected = [
            "Another feedback on RoR application migration @ Shopify with a long paper explaining the different steps / "
            "challenges (showing a few hints / IRL examples). It’s an interesting reading, since the question of Monolith "
            "vs modular […] https://engineering.shopify.com/blogs/engineering/shopify-monolith shared by @tormath1",
            "applications is not easy to answer and there is no generic method to solve it. So, we developed a new tool "
            "called Packwerk to analyze static constant references. […] We’re planning to make Packwerk open source "
            "soon. Stay tuned! I’m definitely looking for to see how they […]",
            "proceed and why not try to make it language agnostic.",
        ]

        tweets = format_tweets(payload)
        self.assertEqual(tweets, expected)


if __name__ == "__main__":
    unittest.main()
