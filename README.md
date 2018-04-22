# minimu
the name came from 'mini music player'

to be a small, hidden and clean lightweight music player

fork from [michaelgundlach/mp3play](https://github.com/michaelgundlach/mp3play), but almost all the code was renewed to support python3 and unicode file name.

### highlight
1. only for python3
2. only for windows
3. now only for mp3
4. still in developing

### target
1. More user friendly
2. Support more music formats

### todo
1. main.py: todo
3. support windows in english (now can't return english error describting)

### how to use

1. play one song
```
import minimu

song=minimu.load(r'example.mp3')

song.play() # play

song.pause() # pause

song.resume() # resume

song.stop() # stop

song.isplaying() # True: play or pause | False: stop

song.volume(50) # set volume%
```

2. play one folder
```
>>> import minimu as mu
>>> # loda mp3s in this folder,show the music list and auto play the first one
>>> l = mu.loadlist(r'testmusic')
0    EMI
1    GodSaveTheQueen
2    NewYork
3    NoFeelings
>>> # show the music list
>>> l.shownames()
0    EMI
1    GodSaveTheQueen
2    NewYork
3    NoFeelings
>>> # play music 6
>>> l.play(6)
>>> l.pause()
>>> l.resume()
>>> l.stop()
>>> l.play()
>>> l.isplaying()
True
>>> l.volume(80)
>>> # play next one
>>> l.next()
>>> # play last one
>>> l.last()
>>> l.stop()
```

---

# minimu-中文
名字取自mini music player

力图成为一个小巧,隐蔽,干净的超轻量音乐播放器

Fork自[michaelgundlach/mp3play](https://github.com/michaelgundlach/mp3play), 但是基本所有代码都已经被更新以支持python3和unicode文件名.

### 注意
1. 只支持python3
2. 只支持windows平台
3. 暂只支持mp3格式
4. 仍在开发中

### 目标
1. 对用户更加友好
2. 支持更多的音乐格式

### todo
1. 完成main.py中的todo
2. 完成以下功能:
    1. 指定文件目录播放
    2. 指定本地歌单播放
    3. 快捷键:播放,暂停,恢复,停止,上一首,下一首,快进,快退,加减音量
    4. 通过歌曲链接播放
    5. 指定包含歌曲链接的歌单播放
3. 支持非中文windows系统

### 如何使用

1. 单曲播放
```
import minimu

song=minimu.load(r'中文路径.mp3')

song.play() # 开始播放

song.pause() # 暂停播放

song.resume() # 恢复播放

song.stop() # 停止播放

song.isplaying() # True:正在播放(包括暂停) False:已停止播放

song.volume(50) # 调节音量至50%
```

2. 文件夹播放
```
>>> import minimu as mu
>>> # 读取文件夹内mp3文件,显示歌曲列表,并自动播放第一首
>>> l = mu.loadlist(r'testmusic')
0    不多
1    大象
2    好威武支持有希望
3    定西
4    方式
5    热河
6    看见
7    鼠说
>>> # 显示歌曲列表
>>> l.shownames()
0    不多
1    大象
2    好威武支持有希望
3    定西
4    方式
5    热河
6    看见
7    鼠说
>>> # 播放歌曲序号6
>>> l.play(6)
>>> l.pause()
>>> l.resume()
>>> l.stop()
>>> l.play()
>>> l.isplaying()
True
>>> l.volume(80)
>>> # 播放下一首
>>> l.next()
>>> # 播放上一首
>>> l.last()
>>> l.stop()
```