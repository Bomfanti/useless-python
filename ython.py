import sys
import time
import random
import string
import os

words = [
    "Initializing", "Syncing", "Resolving", "Fetching", "Decrypting",
    "Allocating", "Verifying", "Processing", "Compiling", "Uploading",
    "Downloading", "Indexing", "Parsing", "Optimizing", "Encrypting",
    "Handshake", "Payload", "Packet", "Stream", "Buffer",
    "Authenticating", "Routing", "Hashing", "Tokenizing",
    "Bootstrapping", "Finalizing", "Stabilizing"
]

titles = [
    "System Loader",
    "Data Pipeline",
    "Secure Channel",
    "Network Core",
    "Runtime Engine",
    "Background Task",
    "Internal Service"
]

headers = [
    "[ CORE MODULE ]",
    "[ NETWORK LAYER ]",
    "[ SECURITY HANDLER ]",
    "[ IO PIPELINE ]",
    "[ MEMORY MANAGER ]",
    "[ TASK SCHEDULER ]"
]

def set_title(title):
    if os.name == "nt":
        os.system(f"title {title}")
    else:
        sys.stdout.write(f"\33]0;{title}\a")
        sys.stdout.flush()

def random_hash(size=8):
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=size))

def clear():
    os.system("cls" if os.name == "nt" else "clear")

counter = 0

while True:
    if counter % 20 == 0:
        set_title(random.choice(titles))
        clear()
        print(random.choice(headers))
        print("-" * 40)

    w = random.choice(words)
    h1 = random_hash(random.randint(6, 12))
    h2 = random_hash(random.randint(6, 12))
    pct = random.randint(0, 100)
    dots = "." * random.randint(1, 5)

    print(f"{w} {h1}->{h2} [{pct}%]{dots}")

    time.sleep(random.uniform(0.5, 0.95))
    counter += 1
