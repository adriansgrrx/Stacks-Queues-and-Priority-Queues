# Using multiprocessing.Queue for Interprocess Communication (IPC)
# Reversing an MD5 Hash on a Single Thread
# MD5 (message-digest algorithm) is a cryptographic protocol used for authenticating messages as well as content verification and digital signatures. 

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