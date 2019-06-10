# -*- coding: utf-8 -*-

import yaml

with open("test.yaml", 'r') as rf:
    s = yaml.load(rf.read())
    print(s)
    # w = {'name': 'fenny'}
    # yaml.dump(w, rf)