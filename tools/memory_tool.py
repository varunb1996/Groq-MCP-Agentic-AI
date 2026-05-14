import json
import os

MEMORY_PATH = "memory/chat_memory.json"


def load_memory():

    if not os.path.exists(MEMORY_PATH):
        return []

    with open(MEMORY_PATH, "r") as f:
        return json.load(f)



def save_memory(message):

    memory = load_memory()

    memory.append(message)

    with open(MEMORY_PATH, "w") as f:
        json.dump(memory, f, indent=4)