#!/usr/bin/env python3
"""Fetch a web page and extract clean, readable text.

Usage:
    python fetch_url.py "https://example.com/article" > page.json

Outputs JSON: {"url", "title", "headings": [...], "text"}.

This is a skeleton. Replace the naive parsing with a real readability
extractor (e.g. trafilatura, readability-lxml) for production use.
"""
import json
import sys
import urllib.request
from html.parser import HTMLParser


class _TextExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.title = ""
        self.headings = []
        self.chunks = []
        self._tag = None

    def handle_starttag(self, tag, attrs):
        self._tag = tag

    def handle_endtag(self, tag):
        self._tag = None

    def handle_data(self, data):
        text = data.strip()
        if not text:
            return
        if self._tag == "title":
            self.title = text
        elif self._tag in ("h1", "h2", "h3"):
            self.headings.append(text)
        elif self._tag in ("p", "li"):
            self.chunks.append(text)


def fetch(url: str) -> dict:
    req = urllib.request.Request(url, headers={"User-Agent": "url-to-video/0.1"})
    with urllib.request.urlopen(req, timeout=20) as resp:
        html = resp.read().decode("utf-8", errors="replace")
    parser = _TextExtractor()
    parser.feed(html)
    return {
        "url": url,
        "title": parser.title,
        "headings": parser.headings,
        "text": "\n".join(parser.chunks),
    }


def main(argv):
    if len(argv) != 2:
        print("usage: fetch_url.py <url>", file=sys.stderr)
        return 2
    print(json.dumps(fetch(argv[1]), ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
