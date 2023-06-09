from __future__ import absolute_import

import os
from got10k.datasets import *

from siamfc import TrackerSiamFC


if __name__ == '__main__':
    seqs = GOT10k(root_dir='D:\\BaiduNetdiskDownload\\GOT-10k', subset='train', return_meta=True)

    tracker = TrackerSiamFC()
    tracker.train_over(seqs)
