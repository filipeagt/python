from pygame import mixer, event
mixer.init()
mixer.music.load('happy-mistake.mp3')
mixer.music.play()
input()
event.wait()