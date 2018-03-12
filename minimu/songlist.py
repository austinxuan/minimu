from .main import Song
import os

"""
todo:
1. 优化代码
2. 添加模式选择: 单曲/列表/循环/随机
"""
class Songlist(object):
    def __init__(self, path):
        self._load=Song
        self._path = path
        self._playingnumber = 0
        self._getsongs()
        self.shownames()
        self.play()

    def _getfiledict(self, ext, *, path=None):
        thedict={}
        ext = ext if ext[0]=='.' else '.'+ext
        path = path.replace( "/","\\") if path else os.path.abspath('.')
        for rootpath,subpaths,files in os.walk(path):
            for file in files:
                filepath, filenameandext = os.path.split(file)
                filename, fileext = os.path.splitext(filenameandext)
                if fileext == ext:
                    thedict[filename]=os.path.join(rootpath,file)
        return thedict

    def _getsongs(self):
        name_path_dict=self._getfiledict('mp3',path=self._path)
        name_list=list(name_path_dict.keys())
        path_list=list(name_path_dict.values())
        self._songnumber=len(name_list)-1
        self._names=dict(zip(range(len(name_list)),name_list))
        self._songs=dict(zip(name_list,[self._load(x) for x in path_list]))

    def shownames(self):
        for x in self._names:
            print(str(x)+'    '+self._names[x])

    def play(self, number=-1):
        self.stop()
        if number!=-1:
            self._playingnumber = number
        self._songs[self._names[self._playingnumber]].play()


    def pause(self):
        self._songs[self._names[self._playingnumber]].pause()

    def resume(self):
        self._songs[self._names[self._playingnumber]].resume()

    def stop(self):
        self._songs[self._names[self._playingnumber]].stop()

    def isplaying(self):
        return self._songs[self._names[self._playingnumber]].isplaying()

    def volume(self, level):
        self._songs[self._names[self._playingnumber]].volume(level)

    def next(self):
        self._songs[self._names[self._playingnumber]].stop()
        self._playingnumber= self._playingnumber + 1 if self._playingnumber != self._songnumber  else 0
        self._songs[self._names[self._playingnumber]].play()

    def last(self):
        self._songs[self._names[self._playingnumber]].stop()
        self._playingnumber= self._playingnumber - 1 if self._playingnumber != 0  else self._songnumber
        self._songs[self._names[self._playingnumber]].play()