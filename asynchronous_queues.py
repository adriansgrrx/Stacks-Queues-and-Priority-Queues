# To fetch data asynchronously, aiohttp library and beautifulsoup4. to parse HTML hyperlinks.

# Asynchronous programming is a type of parallel programming in which a unit of work is allowed to run separately from the primary application thread. When the work is complete, it notifies the main thread about completion or failure of the worker thread.
import sys # It allows operating on the interpreter as it provides access to the variables and functions that interact strongly with the interpreter.
import argparse
import asyncio
from collections import Counter
import aiohttp
from urllib.parse import urljoin
from bs4 import BeautifulSoup
from typing import NamedTuple

class Job(NamedTuple):
    url: str
    depth: int = 1

async def main(args):
    session = aiohttp.ClientSession()
    try:
        links = Counter()
        display(links)
    finally:
        await session.close()

# The argparse module’s support for command-line interfaces is built around an instance of argparse.ArgumentParser. 
def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("url")
    parser.add_argument("-d", "--max-depth", type=int, default=2)
    parser.add_argument("-w", "--num-workers", type=int, default=3)
    return parser.parse_args()

def display(links):
    for url, count in links.most_common():
        print(f"{count:>3} {url}")

# asynchronous function or also known as coroutine changes the behavior of the function call.
if __name__ == "__main__":
    asyncio.run(main(parse_args()))

# EXCLUSIVELY FOR HTML
async def fetch_html(session, url):
    async with session.get(url) as response:
        if response.ok and response.content_type == "text/html":
            return await response.text()

def parse_links(url, html):
    soup = BeautifulSoup(html, features="html.parser")
    for anchor in soup.select("a[href]"):
        href = anchor.get("href").lower()
        if not href.startswith("javascript:"):
            yield urljoin(url, href)