#!/usr/bin/env python
import time
import sys

for i in range(25):
    print(i)
    # Flushing to makes sure it's pushed to stdout
    sys.stdout.flush()
    time.sleep(0.2)