#!/usr/bin/env python

import os
import requests
import subprocess

try:
    assert(requests.get("http://www.google.com").status_code == 200)
    subprocess.run(['/home/z/.config/polybar/gmail/run.py'])

except Exception as foo:
    print('')

