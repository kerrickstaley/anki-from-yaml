#!/usr/bin/env python3
import genanki
import yaml
import argparse
import random

parser = argparse.ArgumentParser('Generate an Anki deck from a YAML file')
parser.add_argument('in_file', help='Input YAML file')

def main(args):
    with open(args.in_file) as f:
        data = yaml.safe_load(f)

    deck = genanki.Deck(random.randrange(1 << 31, 1 << 32), data['name'])

    for note_data in data['notes']:
        note = genanki.Note(
            model=genanki.builtin_models.CLOZE_MODEL,
            fields=[note_data['cloze'], note_data.get('extra', '')],
            guid=note_data.get('guid'),
            tags=note_data.get('tags'))

        deck.add_note(note)

    deck.write_to_file(args.in_file.removesuffix('.yaml') + '.apkg')

if __name__ == '__main__':
    args = parser.parse_args()
    main(args)
