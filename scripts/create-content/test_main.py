#!/usr/bin/env python3
import unittest

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


if __name__ == "__main__":
    unittest.main()
