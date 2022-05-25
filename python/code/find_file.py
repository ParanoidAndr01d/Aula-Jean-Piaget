import os
fileType = '.mp4'

anyFile = os.listdir('desktop')
for file in anyFile:
  if file.endswith(fileType):
    print(file)