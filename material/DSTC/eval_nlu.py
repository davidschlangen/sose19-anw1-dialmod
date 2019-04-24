# coding: utf-8

from __future__ import division, print_function
import json
import argparse


def nlu(injson, goldjson, errorjson):
    with open(injson, 'r') as f:
        predicted_data = json.load(f)
    with open(goldjson, 'r') as f:
        gold_data = json.load(f)

    out = []

    correct = 0

    # this is assuming that they are in same order
    # you could also go by IDs and evaluate only those
    # turns which are both in predicted and gold
    for n, (pred, gold) in enumerate(zip(predicted_data, gold_data)):
        dial_id = pred['dial_id']
        turn_id = pred['turn_id']
        utt = pred['usr_utt']

        pred_sem = pred['usr_sem']
        gold_sem = gold['usr_sem']
        # now compare them in some way
        #  this is the strictest, and least informative way:
        if pred_sem == gold_sem:
            correct += 1

        out.append({'dial_id': dial_id,
                    'turn_id': turn_id,
                    'usr_utt': utt,
                    'errors': 'I DO NOT MAKE ERRORS'})

    with open(errorjson, 'w') as f:
        json.dump(out, f, indent=2)

    print('Accuracy: {:.4f}'.format(correct / n))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Evaluate NLU component')
    parser.add_argument('input',
                        help='the file with the predictions')
    parser.add_argument('gold',
                        help='the respective gold standard info')
    parser.add_argument('errorlog',
                        help='where to write info about errors')
    args = parser.parse_args()

    nlu(args.input, args.gold, args.errorlog)
