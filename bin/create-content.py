#!/usr/bin/env python3
import sys
import json

template = """---
title: {title}
date: {created_at}
link: {url}
github_username: {user}
---
{description}
"""


def slugify(date, title):
    slug = title.lower()
    slug = slug.replace(" ", "-")
    date = date[:10]
    return f"content/links/{date}-{slug}.md"


def main(filename):
    with open(filename, "r") as f:
        data = json.load(f)
    title = data["issue"]["title"]
    created_at = data["issue"]["created_at"]
    user = data["issue"]["user"]["login"]
    body = data["issue"]["body"]
    url = body.splitlines()[0].replace("url: ", "")
    description = "\n".join(body.splitlines()[2:])
    post_filename = slugify(created_at, title)
    content = template.format(
        title=title, created_at=created_at, url=url, user=user, description=description
    )
    print(post_filename)
    print(content)
    with open(post_filename, "w+") as f:
        print(content, file=f)


if __name__ == "__main__":
    filename = sys.argv[1]
    main(filename)
