# -*- coding: utf-8 -*-

import os

if os.name == 'nt':
    from .main import Song as _PlatformSpecificSong
else:
    raise Exception("can't run on this system.")

def load(filename):
    # 使用minimu.load()来获取一个Song的实例
    from .main import Song
    return Song(filename)