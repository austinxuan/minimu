# -*- coding: utf-8 -*-

import os

# 将AudioClip import as _PlatformSpecificAudioClip,并在下面另外class一个AudioClip
# 是为了配适不同的操作系统,__init__调用的都是已经封装好的方法
# 现有版本: 1. windows 
# TODO:添加配适linux的_PlatformSpecificAudioClip:
# elif os.name == 'posix':
#    from .linux import AudioClip as _PlatformSpecificAudioClip
if os.name == 'nt':
    from .windows import AudioClip as _PlatformSpecificAudioClip
else:
    raise Exception("can't run on this operating system.")

def load(filename):
    """Return an AudioClip for the given filename."""
    # 这样就可以使用minimu.load()来获取一个AudioClip的实例
    return AudioClip(filename)

class AudioClip(object):
    # 使用__slots__变量，来限制该class实例能添加的属性
    __slots__ = ('_clip')

    def __init__(self, filename):
        """Create an AudioClip for the given filename."""
        # 给AudioClip添加_clip属性,_表示这是一个私有变量
        # _clip属性等于_PlatformSpecificAudioClip类
        self._clip = _PlatformSpecificAudioClip(filename)

    # 以下都是把_PlatformSpecificAudioClip的方法绑定到AudioClip上,并增加了错误处理

    def play(self, start_ms=None, end_ms=None):
        """
        Start playing the audio clip, and return immediately. Play from
        start_ms to end_ms if either is specified; defaults to beginning
        and end of the clip.  Returns immediately.  If end_ms is specified
        as smaller than start_ms, nothing happens.
        """
        if end_ms != None and end_ms < start_ms:
            raise Exception("end_ms should be greater than start_ms")
        else:
            return self._clip.play(start_ms, end_ms)

    def volume(self, level):
        """Sets the volume between 0 and 100."""
        assert level >=0 and level <= 100
        return self._clip.volume(level)

    def isplaying(self):
        """Returns True if the clip is currently playing.  Note that if a
        clip is paused, or if you called play() on a clip and playing has
        completed, this returns False."""
        return self._clip.isplaying()

    def pause(self):
        """Pause the clip if it is currently playing."""
        return self._clip.pause()

    def unpause(self):
        """Unpause the clip if it is currently paused."""
        return self._clip.unpause()

    def ispaused(self):
        """Returns True if the clip is currently paused."""
        return self._clip.ispaused()

    def stop(self):
        """Stop the audio clip if it is playing."""
        return self._clip.stop()

    # seconds方法来自milliseconds方法
    def seconds(self):
        """
        Returns the length in seconds of the audio clip, rounded to the
        nearest second.
        """
        return int(round(float(self.milliseconds()) / 1000))

    def milliseconds(self):
        """Returns the length in milliseconds of the audio clip."""
        return self._clip.milliseconds()
