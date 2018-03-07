#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import time
import minimu

testmusicdir=os.getenv('testmusicdir')
os.chdir(testmusicdir)
clip=minimu.load('test.mp3')
clip.play()
time.sleep(clip.seconds())