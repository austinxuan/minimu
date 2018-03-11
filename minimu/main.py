import random, sys
from ctypes import windll, c_buffer

class Song(object):
    def __init__(self, filename):
        self._mci = windll.winmm.mciSendStringW
        self._mcierr = windll.winmm.mciGetErrorStringA

        self.filename = filename
        self._alias = 'song_{}'.format(random.random())

        self._send('open {} alias {}'.format(self.filename, self._alias ))
        self._send('set {} time format milliseconds'.format(self._alias))
        # todo: 以下两行代码无法返回正确结果
        mcicode, mcistr=self._send('status {} length'.format(self._alias))
        self._length_ms = int(mcistr)

    def _send(self, command):
        buffer = c_buffer(1024)
        mcicode = self._mci(command, buffer, 1023, 0)
        mcistr = buffer.value.decode('gbk')
        if mcicode:
            self._mcierr(int(mcicode), buffer, 1023)
            mcistr = buffer.value.decode('gbk')
            print('Error: {}'.format(mcistr))
        return mcicode, mcistr

    def play(self):
        self._send('play {}'.format(self._alias))

    def pause(self):
        self._send('pause {}'.format(self._alias))

    def resume(self):
        self._send('resume {}'.format(self._alias))

    def stop(self):
        self._send('stop {}'.format(self._alias))
        # 不明白seek指令
        self._send('seek {} to start'.format(self._alias))

    def _mode(self):
        mcicode, mcistr = self._send('status {} mode'.format(self._alias))
        # 返回值: p:正在播放(包括暂停) s:停止播放 
        # todo: 检测暂停
        return mcistr

    def isplaying(self):
        return self._mode() == 'p'

    # 无法返回正确值
    # todo: 返回正确值
    def milliseconds(self):
        return self._length_ms

    # 无法返回正确值
    # todo: 返回正确值
    def seconds(self):
        return int(float(self.milliseconds()) / 1000)

    def volume(self, level):
        # todo: 添加错误处理
        # assert level >=0 and level <= 100
        self._send('setaudio {} volume to {}'.format(self._alias, level * 10))

    # del Song的时候执行
    def __del__(self):
        if self.isplaying():
            self.stop()
        else:
            self._send('close {}'.format(self._alias))