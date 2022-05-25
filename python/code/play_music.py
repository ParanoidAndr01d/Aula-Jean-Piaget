from pygame import mixer

mixer.init()
mixer.music.load('musica.mp3')
mixer.music.play()
pygame.event.wait()