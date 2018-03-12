# -*- coding: utf-8 -*-

import os

if os.name != 'nt':
    raise Exception("can't run on this system.")

def load(filename):
    from .main import Song
    return Song(filename)

def loadlist(path):
    from .songlist import Songlist
    return Songlist(path)

"""
todo:
添加: 播放url,生成歌单,播放歌单(包含本地歌曲/url的配置文件)
"""