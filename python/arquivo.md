# Desafio 1

1) Uma certa empresa foi intimada pela justiça a fornecer arquivos e registros específicos na próxima semana, por isso, crie um programa que encontre-os:

```python
import os
fileType = '.mp4'

anyFile = os.listdir('desktop')
for file in anyFile:
  if file.endswith(fileType):
    print(file)
```