#!/usr/bin/env python3

import argparse
from jinja2 import Environment, FileSystemLoader

# There are some illegal characters
def clean(input):
    output = input.replace('\u001f', '')
    return output

if __name__ == "__main__":
    argparser = argparse.ArgumentParser(description='Generate XML file.')
    argparser.add_argument('input', type=str)
    argparser.add_argument('output', type=str)
    args = argparser.parse_args()

    entries = []
    with open(args.input) as f:
        content = f.readlines()
        for line in content:
            try:
                word, explanation = line.split('\t\t')

                word = clean(word)
                explanation = clean(explanation)

                entries.append({
                    'word': word,
                    'explanation': explanation,
                })
            except:
                print("Bad line: %s" % line)
    print("Loaded " + str(len(entries)) + " entries.")

    env = Environment(loader=FileSystemLoader("./"),
                      trim_blocks=True, lstrip_blocks=True)
    template = env.get_template("template.xml")

    with open(args.output, "w") as f:
        f.write(template.render(entries=entries))
