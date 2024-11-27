#!/usr/bin/env python
__author__ = 'surister'
__author_contact__ = 'github/surister'

import pathlib
import sys

if len(sys.argv) < 2:
    raise Exception('Expected one argument with ".../project/node_modules/@vue/" path')
 
if 'vue' not in sys.argv[1]:
    raise ValueError('Hey, are you sure you are passing a @vue path?')

node_vue_path = pathlib.Path(sys.argv[1])


for folder in node_vue_path.iterdir():
    (node_vue_path / folder / 'locales/').mkdir(exist_ok=True)