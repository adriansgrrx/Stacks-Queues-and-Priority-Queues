# Using multiprocessing.Queue for Interprocess Communication (IPC)
# Reversing an MD5 Hash on a Single Thread
# MD5 (message-digest algorithm) is a cryptographic protocol used for authenticating messages as well as content verification and digital signatures. 

import time
from hashlib import md5
from itertools import product
from string import ascii_lowercase
import multiprocessing
from dataclasses import dataclass

# Formula encapsulation
class Combinations:
    def __init__(self, alphabet, length):
        self.alphabet = alphabet
        self.length = length

    def __len__(self):
        return len(self.alphabet) ** self.length
    # This represents a collection of alphabet letter combinations with a given length. 
    def __getitem__(self, index):
        if index >= len(self):
            raise IndexError
        return "".join(
            self.alphabet[
                # A formula that determines the character at a given position in a combination specified by an index
                (index // len(self.alphabet) ** i) % len(self.alphabet)
            ]
            for i in reversed(range(self.length))
        )
# A class that Python will serialize and place on the input queue for worker processes to consume
@dataclass(frozen=True)
class Job:
    combinations: Combinations
    start_index: int
    stop_index: int

    def __call__(self, hash_value):
        for index in range(self.start_index, self.stop_index):
            text_bytes = self.combinations[index].encode("utf-8")
            hashed = md5(text_bytes).hexdigest()
            if hashed == hash_value:
                return text_bytes.decode("utf-8")

# Communicating in Full-Duplex Mode
# To define a worker process, Process class will be extended, which provides the familiar .run() method.
class Worker(multiprocessing.Process):
    def __init__(self, queue_in, queue_out, hash_value):
        super().__init__(daemon=True)
        self.queue_in = queue_in
        self.queue_out = queue_out
        self.hash_value = hash_value

    def run(self):
        while True:
            job = self.queue_in.get()
            if plaintext := job(self.hash_value):
                self.queue_out.put(plaintext)
                break

# will define a function that’ll try to reverse an MD5 hash value provided as the first argument. 
def reverse_md5(hash_value, alphabet=ascii_lowercase, max_length=6):
    for length in range(1, max_length + 1):
        for combination in Combinations(alphabet, length):
            text_bytes = "".join(combination).encode("utf-8")
            hashed = md5(text_bytes).hexdigest()
            if hashed == hash_value:
                return text_bytes.decode("utf-8")

# Distributing Workload Evenly in Chunks
def chunk_indices(length, num_chunks):
    start = 0
    while num_chunks > 0:
        num_chunks = min(num_chunks, length)
        chunk_size = round(length / num_chunks)
        yield start, (start := start + chunk_size)
        length -= chunk_size # rounding the subsequent chunk lengths, those with varying lengths end up nicely interleaved
        num_chunks -= 1

# call the function with a sample MD5 hash value passed as an argument and measure its execution time using a Python timer.
def main():
    t1 = time.perf_counter()
    text = reverse_md5("a9d1cbf71942327e98b40cf5ef38a960") # sample hash value
    print(f"{text} (found in {time.perf_counter() - t1:.1f}s)")

if __name__ == "__main__":
    main()