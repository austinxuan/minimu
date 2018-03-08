# -*- coding: utf-8 -*-

# 使用dtypes.windll调用win32API

import random

from ctypes import windll, c_buffer

class _mci:
    def __init__(self):
        self.w32mci = windll.winmm.mciSendStringA
        self.w32mcierror = windll.winmm.mciGetErrorStringA

    def send(self, command):
        buffer = c_buffer(255)
        errorcode = self.w32mci(str(command).encode('utf-8'), buffer, 254, 0)
        if errorcode:
            return errorcode, self.get_error(errorcode)
        else:
            return errorcode, buffer.value

    def get_error(self, error):
        error = int(error)
        buffer = c_buffer(255)
        self.w32mcierror(error, buffer, 254)
        return buffer.value

    def directsend(self, txt):
        (err, buf) = self.send(txt)
        if err != 0:
            print('Error {} for "{}": {}'.format(str(err), txt, buf))
        return (err, buf)

# TODO: detect errors in all mci calls
class AudioClip(object):
    def __init__(self, filename):
        self.filename = filename
        self._alias = 'mp3_{}'.format(str(random.random()))

        self._mci = _mci()

        self._mci.directsend(r'open "{}" alias {}'.format(filename, self._alias ))
        self._mci.directsend('set {} time format milliseconds'.format(self._alias))

        err, buf=self._mci.directsend('status {} length'.format(self._alias))
        self._length_ms = int(buf)

    def volume(self, level):
        """Sets the volume between 0 and 100."""
        self._mci.directsend('setaudio {} volume to {}'.format(self._alias, level * 10))

    def play(self, start_ms=None, end_ms=None):
        start_ms = 0 if not start_ms else start_ms
        end_ms = self.milliseconds() if not end_ms else end_ms
        err,buf=self._mci.directsend('play {} from {} to {}'.format(self._alias, start_ms, end_ms))

    def isplaying(self):
        return self._mode() == 'playing'

    def _mode(self):
        err, buf = self._mci.directsend('status {} mode'.format(self._alias))
        return buf

    def pause(self):
        self._mci.directsend('pause {}'.format(self._alias))

    def unpause(self):
        self._mci.directsend('resume {}'.format(self._alias))

    def ispaused(self):
        return self._mode() == 'paused'

    def stop(self):
        self._mci.directsend('stop {}'.format(self._alias))
        self._mci.directsend('seek {} to start'.format(self._alias))

    def milliseconds(self):
        return self._length_ms

    # TODO: this closes the file even if we're still playing.
    # no good.  detect isplaying(), and don't die till then!
    def __del__(self):
        self._mci.directsend('close {}'.format(self._alias))
