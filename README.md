# MyRaspStreamer
most simple streaming solution. Focus is on absolute ease of use.

# Hardware
Raspberry Zero W, as ist has WLAN support from the start and is small enough to fit in a handy casing
## Amplifier
![Amplifier PAM 8403](PAM8403.jpg)

after several tries I found that the PAM8403 ist strong enough an works well with 5 volts [EBay link to the ampifier](http://www.ebay.de/itm/Super-Mini-PAM8403-Digitaler-Verstärker-Platine-D-Digitalverstärker-Bord-B98B/)

## DAC
![DAC PCM5102 A](PCM5102a.jpg)

|PCM5102a|Func|RPi 0 Pin|GPIO|Func|
|--------|--------|--------|--------|--------|
|VCC|Not connected|--|--|--|
|3.3 V|3.3 V|1|X|3.3V|
|GND|GND|39|X|GND|
|FLT|GND|--|--|--|
|DMP|GND|--|--|--|
|SCL|SCL|5|GPIO3|SCL1 I2C|
|BCK|BCK|12|GPIO18|PCM_CLK|
|DIN|Data|40|GPIO21|??|
|LCK|LCK|35|GPIO19|??|
|FMT|GND|--|--|--|
|XMT|3.3V|--|--|--|

RPi Zero does not give easy access to PWM pins. Using a cheap pHat DAC doe convert to analog signal is a good way as the audio quality is also better as with PWM. this DAC can be easily configured to mimic the HIFIBerry DAC [AliExpress Link to the DAC](https://de.aliexpress.com/item/Raspberry-Pi-pHAT-Sound-Card-I2S-interface-PCM5102-DAC-Module-24-bit-Audio-Board-With-Stereo/32744871341.html)
## USB Power plug
Because the RPi USB Socket is not easily accessible in the small case [AliExpress Link to the USB Plug](https://www.aliexpress.com/item/10pcs-MICRO-USB-to-DIP-Adapter-5pin-Female-Connector-B-Type-PCB-Converter/32720363831.html) 

# Software
## solution with volumio 2 (instructions valid for volumio 2.348)
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
[fun script] (home/volumio/control.py)

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

check, that espeak works correctly (french for me;-)
```
espeak -vfr 'Box Ok' --stdout | aplay -Dsoftvol
```

changing keyboard layout fo french
```
sudo apt-get install console-data
loadkeys fr
```
