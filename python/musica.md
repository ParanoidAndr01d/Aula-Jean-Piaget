# Desafio 2

2) Um amigo próximo pediu para desenvolver um trecho de código capaz de reproduzir um efeito sonoro ou uma música.

```python

from pygame import mixer
mixer.init()
mixer.music.load('musica.mp3')
mixer.music.play()
pygame.event.wait()

```