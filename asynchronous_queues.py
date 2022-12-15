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
    # adding the .__lt__() special method to the Job class, to which the less than (<) operator delegates when comparing two job instances:
    def __lt__(self, other):
        if isinstance(other, Job):
            return len(self.url) < len(other.url)

# Updated main function for Queue FIFO to execute
async def main(args):
    session = aiohttp.ClientSession()
    try:
        links = Counter()
        # queue = asyncio.Queue() # instantiates an asynchronous FIFO queue.
        queue = asyncio.LifoQueue() # instantiates an asynchronous LIFO queue.

        # create a number of worker coroutines wrapped in asynchronous tasks that start running as soon as possible in the background on the event loop.
        tasks = [
            asyncio.create_task(
                worker(
                    f"Worker-{i + 1}",
                    session,
                    queue,
                    links,
                    args.max_depth,
                )
            )
            for i in range(args.num_workers)
        ]

        await queue.put(Job(args.url)) # puts the first job in the queue, which kicks off the crawling.
        await queue.join() # causes the main coroutine to wait until the queue has been drained and there are no more jobs to perform.

        # do a graceful cleanup when the background tasks are no longer needed.
        for task in tasks:
            task.cancel()

        await asyncio.gather(*tasks, return_exceptions=True)

        display(links)
    finally:
        await session.close()

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

# The worker sits in an infinite loop, waiting for a job to arrive in the queue. After consuming a single job, the worker can put one or more new jobs with a bumped-up depth in the queue to be consumed by itself or other workers.
async def worker(worker_id, session, queue, links, max_depth):
    print(f"[{worker_id} starting]", file=sys.stderr) # stderr -> Standard error – The user program writes error information to this file-handle.
    while True:
        url, depth = await queue.get()
        links[url] += 1
        try:
            if depth <= max_depth:
                print(f"[{worker_id} {depth=} {url=}]", file=sys.stderr)
                if html := await fetch_html(session, url): # The walrus operator (:=) lets you await an HTTP response, check if the content was returned, and assign the result to the html variable in a single expression.
                    for link_url in parse_links(url, html):
                        await queue.put(Job(link_url, depth + 1))
        except aiohttp.ClientError:
            print(f"[{worker_id} failed at {url=}]", file=sys.stderr)
        finally:
            queue.task_done()

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