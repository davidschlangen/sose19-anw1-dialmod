# coding: utf-8

import json
import sys

sys.path.append('./')
from _dstc2_scripts.dataset_walker import dataset_walker


for data_source in ['dstc2_dev', 'dstc2_train']:
    dataset = dataset_walker(data_source, dataroot="_Data/", labels=True)
    out = []
    for m, call in enumerate(dataset):
        for n, (turn, label) in enumerate(call):
            this_turn = []
            usr_utt = label['transcription']
            usr_sem = label['semantics']['json']
            out.append({
                'dial_id': m,
                'turn_id': n,
                'usr_utt': usr_utt,
                'usr_sem': usr_sem
                })
    with open('usr_sem-' + data_source + '.json', 'w') as f:
        json.dump(out, f, indent=2)

    with open('usr_sem-' + data_source + '-test.json', 'w') as f:
        json.dump([{k: v for k, v in d.items() if k != 'usr_sem'} for d in out],
                  f, indent=2)
