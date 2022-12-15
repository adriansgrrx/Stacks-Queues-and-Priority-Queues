# To fetch data asynchronously, aiohttp library and beautifulsoup4. to parse HTML hyperlinks.
import argparse
import asyncio
from collections import Counter
import aiohttp

async def main(args):
    session = aiohttp.ClientSession()
    try:
        links = Counter()
        display(links)
    finally:
        await session.close()