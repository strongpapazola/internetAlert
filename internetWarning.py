from urllib.request import urlopen
import time
from os import system

def internet_on():
 try:
  urlopen('https://www.google.com', timeout=1)
  return True
 except:
  return False

while True:
 time.sleep(1)
 data = ''
 if internet_on() == False:
  data = 'true'
 else:
  data = ''
 if data == 'true':
  system('play -q error.mp3')
