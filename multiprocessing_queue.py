# Using multiprocessing.Queue for Interprocess Communication (IPC)
# Reversing an MD5 Hash on a Single Thread
# MD5 (message-digest algorithm) is a cryptographic protocol used for authenticating messages as well as content verification and digital signatures. 

import time
from hashlib import md5
from itertools import product
from string import ascii_lowercase

# will define a function that’ll try to reverse an MD5 hash value provided as the first argument. 
def reverse_md5(hash_value, alphabet=ascii_lowercase, max_length=6):
    for length in range(1, max_length + 1):
        for combination in product(alphabet, repeat=length):
            text_bytes = "".join(combination).encode("utf-8")
            hashed = md5(text_bytes).hexdigest()
            if hashed == hash_value:
                return text_bytes.decode("utf-8")
                
# call the function with a sample MD5 hash value passed as an argument and measure its execution time using a Python timer.
def main():
    t1 = time.perf_counter()
    text = reverse_md5("a9d1cbf71942327e98b40cf5ef38a960") # sample hash value
    print(f"{text} (found in {time.perf_counter() - t1:.1f}s)")

if __name__ == "__main__":
    main()