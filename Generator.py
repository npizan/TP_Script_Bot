import markovify
import os
import random


def gen_twitter_sentence(filename=None):
    if filename is None:
        filename = pick_speaker()
    else:
        filename = f"Scripts/{filename}"
    twit_max = 280
    desc = ""
    with open(filename, encoding="utf8") as f:
        desc = f"[{f.readline().strip()}]: "
        text = f.read()
    text_model = markovify.Text(text)
    return f"{desc}{text_model.make_short_sentence(twit_max - len(desc))}"


def pick_speaker():
    script = random.choice(os.listdir("Scripts"))
    return f"Scripts/{script}"
