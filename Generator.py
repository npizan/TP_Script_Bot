import markovify


def gen_twitter_sentence(filename):
    twit_max = 280
    desc = ""
    with open(filename) as f:
        desc = f"[{f.readline().strip()}]: "
        text = f.read()
    text_model = markovify.Text(text)
    return f"{desc}{text_model.make_short_sentence(twit_max - len(desc))}"
