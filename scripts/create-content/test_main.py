#!/usr/bin/env python3
import unittest
from unittest import mock
from io import StringIO

from main import main
from main import slugify


class TestSlugyFunction(unittest.TestCase):
    def test_happy_path(self):
        date = "2020-10-02"
        title = "This is a title"
        expected = "content/links/2020-10-02-this-is-a-title.md"
        output = slugify(date, title)
        self.assertEqual(expected, output)

    def test_single_quote(self):
        date = "2020-10-02"
        title = "It's a title"
        expected = "content/links/2020-10-02-its-a-title.md"
        output = slugify(date, title)
        self.assertEqual(expected, output)

    def test_single_quote_utf(self):
        date = "2020-10-02"
        title = "Under Deconstruction: The State of Shopify’s Monolith"
        expected = "content/links/2020-10-02-under-deconstruction-the-state-of-shopifys-monolith.md"
        output = slugify(date, title)
        self.assertEqual(expected, output)

    def test_question_mark(self):
        date = "2020-10-02"
        title = "how they test ?"
        expected = "content/links/2020-10-02-how-they-test.md"
        output = slugify(date, title)
        self.assertEqual(expected, output)

    def test_percent_sign(self):
        date = "2020-10-02"
        title = "Why is 100% reliability the wrong target?"
        expected = "content/links/2020-10-02-why-is-100-reliability-the-wrong-target.md"
        output = slugify(date, title)
        self.assertEqual(expected, output)


class TestMain(unittest.TestCase):
    @mock.patch("sys.stdout", new_callable=StringIO)
    def test_parse_issue(self, mock_stdout):
        json_data = r"""
            {
                "issue": {
                    "title": "First article",
                    "created_at": "2020-09-12T11:19:56Z",
                    "user": {
                        "login": "pabluk"
                    },
                    "body": "url: https://example.com\r\nhashtags: #hash1,#hash2\r\n---\r\nMarkdown content..."
                }
            }"""
        expected = """content/links/2020-09-12-first-article.md
---
title: "First article"
date: 2020-09-12T11:19:56Z
github_username: pabluk
twitter_username: pabluk
link: https://example.com
hashtags: #hash1,#hash2
---
Markdown content...

"""
        with mock.patch("main.open", mock.mock_open(read_data=json_data)):
            main(None)
            self.assertEqual(expected, mock_stdout.getvalue())


if __name__ == "__main__":
    unittest.main()
