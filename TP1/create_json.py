import json


def process_line(line: str):
    line = line.replace("<br />", "\n").replace('""', '"')
    return line[1:]


reviews = []
# id and review
with open("reviews", "r") as f:
    lines = f.readlines()
    for i, line in enumerate(lines):
        reviews.append({"id": i, "review": process_line(line)})

with open("reviews.json", "w") as f2:
    json.dump(reviews, f2, indent=4)
