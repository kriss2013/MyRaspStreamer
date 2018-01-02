# sudo apt-get install python-pip python-gpiozero espeak
# sudo pip install pyalsaaudio

from gpiozero import Button
from signal import pause
import alsaaudio
import os
import time
import json
import subprocess



mixer = alsaaudio.Mixer('SoftMaster')
mute_button = Button(26)

muted = True
j = json.loads(subprocess.check_output(['volumio', 'status']))
status = j['status']

volume_left, volume_right = mixer.getvolume()
print("Volume: L: %d%%    R: %d%%" % (volume_left, volume_right))
os.system("volumio volume 35")
os.system("espeak -vfr 'Lalie Box Ok' --stdout | aplay -Dsoftvol")

def mute():
  global volume_left, volume_right, muted, status

  j = json.loads(subprocess.check_output(['volumio', 'status']))
  status = j['status']
  print("got status: ")
  print (status)

  if status=='stop':
    print("start playing")
    muted = False
    os.system("espeak -vfr 'mise en marche' --stdout | aplay -Dsoftvol")
    os.system("volumio play")
    # mixer.setvolume(volume_left, 0)
    # mixer.setvolume(volume_right, 1)
  else:
    print("stop playing")
    muted = True
    os.system("volumio stop")
    os.system("espeak -vfr 'stop' --stdout | aplay -Dsoftvol")
    # mixer.setvolume(0, 0)
    # mixer.setvolume(0, 1)

mute_button.when_pressed = mute

print("Ready to receive commands!")

while True:
        if 1==0:
                universeConsistency=False
