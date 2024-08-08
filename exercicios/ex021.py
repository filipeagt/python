from pygame import mixer as mp3
mp3.init()
mp3.music.load('happy-mistake.mp3')
mp3.music.play()
while mp3.music.get_busy() == True:
    continue