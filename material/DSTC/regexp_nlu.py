# coding: utf-8

import json
import argparse


def nlu(injson, outjson):
    with open(injson, 'r') as f:
        data = json.load(f)

    out = []

    for turn in data:
        dial_id = turn['dial_id']
        turn_id = turn['turn_id']
        utt = turn['usr_utt']
        # now do your magic with the utterance...
        # you should produce output with the following structure
        utt_sem = \
            [
                {
                    'act': 'inform',
                    'slots':
                    [
                        ['food', 'swedish']
                    ]
                }
            ]  # this is fake, obviously
        out.append({'dial_id': dial_id,
                    'turn_id': turn_id,
                    'usr_utt': utt,
                    'usr_sem': utt_sem})

    with open(outjson, 'w') as f:
        json.dump(out, f, indent=2)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='RegExp-based NLU component for Cambridge Restaurant Domain')
    parser.add_argument('input',
                        help='the JSON file with the utterances')
    parser.add_argument('output',
                        help='where to write the output with the DAs added')
    args = parser.parse_args()

    nlu(args.input, args.output)
