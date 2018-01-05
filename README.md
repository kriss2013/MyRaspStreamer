# MyRaspStreamer
most simple streaming solution. Focus is on absolute ease of use.

# Hardware
Raspberry 3, as ist has WLAN support from the start  
![Amplifier PAM 8403](PAM8403.jpg)
![DAC PCM5102 A](PCM5102a.jpg)

# solution with volumio 2 (instructions valid for volumio 2.348)
- volumio -> http://volumio.org. 2 users are created: root and volumio. Both with volumio as password.
- Select HIFIBerry DAC as output
- use the volumio gui to put one radio stream in "My Web Radio" (was http://direct.franceinter.fr/live/franceinter-midfi.mp3)
- put the radio in the playing queue (pull down menu on the right of the radio entry in "My Web Radio" -> "add to queue")
- Enable SSH on volumio (local.IP/dev then click enable)
- install cron job in order to stop and restart the radio during the night. All as root (using f.i. sudo)
``` bash
apt-get update && apt-get install -y cron
```
- reboot in the night
```bash
  sudo crontab -e
  0 3 * * * /sbin/init 6        
```
full path to init is necessary, otherwise the job will not run
- activate "GPIO Plugins" and set "Play/pause" (button 26) , volume + (button 6), Volume - (button 5)

## Optional, fun script
- Install script above. Ths script is adapted from https://learn.adafruit.com/boomy-pi-airplay/software 
Espeak is easyer than festival to play something through the softvolume device (in order to controll volume with software, as the DAC has no hardware controlled volume)
Espeak works in french
```bash
sudo apt-get install python-pip python-gpiozero espeak
sudo apt-get install libpython-dev
sudo pip install pyalsaaudio
```
- enable softmixer from alsa stack. Edit /var/lib/alsa/asound.state f.i. with nano
```
sudo nano /var/lib/alsa/asound.state
```
put a code like this one
```
      control.7 {
                iface MIXER
                name SoftMaster
                value.0 34
                value.1 34
                comment {
                        access 'read write user'
                        type INTEGER
                        count 2
                        range '0 - 99'
                        tlv '0000000100000008ffffec7800000032'
                        dbmin -5000
                        dbmax -50
                        dbvalue.0 -3300
                        dbvalue.1 -3300
                }
```
at the appropriate place (clear once the file is edited)  
one edited tha changes must be loaded ba alsa
```
sudo alsactl restore
```
**note:** The new volume control won't appear immediately! Only after the first usage of the newly defined device (e.g. with speaket-test command described below), should amixer controls | grep <control name> display your new control. more background info on the softmixer here: https://alsa.opensrc.org/Softvol and https://alsa.opensrc.org/How_to_use_softvol_to_control_the_master_volume

## some trouble shooting
check, that the alsa layer has access to the speaker (through the DAC and the amplifier)
```
speaker-test -Dplug:softvol -t wav -c 2
```
the system should say "front right, front left" and loop indefinitely  

The following command should show a line with "SoftMaster" as a control, possibly "numid=7,iface=MIXER,name='SoftMaster'"
```
amixer controls
```
if not may be the edit on /var/lib/alsa/asound.state was not successful?
    
work in progress: https://docs.google.com/document/d/1TDSatWPPN96Mer0wqnUFBJojLpwfW_XxlmbxklHs84c/edit?usp=sharing
