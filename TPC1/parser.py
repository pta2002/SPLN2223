from bs4 import BeautifulSoup
import re
import json
import sys

bs_content = None
with open("medicina.xml", "r") as file:
    content = file.readlines()
    bs_content = BeautifulSoup("".join(content), features="xml")

for page in bs_content.find_all("page"):
    text_nodes = page.find_all("text")
    if (
        len(text_nodes) >= 2
        and text_nodes[0].getText() + text_nodes[1].getText() == "Vocabulario"
    ):
        current = {}
        phase = 0
        current_language = None
        current_word = ""
        for node in text_nodes:
            if (text := node.getText().strip()) != "":
                if n := node.find("b"):
                    if current != {}:
                        print(json.dumps(current))
                        current = {}
                    else:
                        current_word += node.getText()
                    phase = 0
                elif phase == 0 and current_word != "":
                    current_word = current_word.strip()
                    if m := re.match(r"^(\d+)\s+.*", current_word):
                        current["number"] = int(m.group(1))
                        groups = list(filter(None, current_word.split(" ")))
                        current["name"] = " ".join(groups[1:-1])
                        current["type"] = groups[-1]
                        phase = 1
                    else:
                        phase = 4
                        current["name"] = current_word
                    current_word = ""
                if phase == 1:
                    current["category"] = text
                    phase = 2
                elif phase == 2:
                    if text.startswith("SIN.-"):
                        current["synonyms"] = text[5:]
                    else:
                        current_language = text
                        phase = 3
                elif phase == 3:
                    current[current_language] = text
                    phase = 2
                elif phase == 4:
                    if text.startswith("Vid."):
                        current["definition"] = text[5:].strip()
                        phase = 0
                    else:
                        print("ERROR: " + text, json.dumps(current))
                        sys.exit(1)
