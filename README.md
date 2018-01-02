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
 - Enable SSH on volumio (local.IP/dev then click enable)

    
    
work in progress: https://docs.google.com/document/d/1TDSatWPPN96Mer0wqnUFBJojLpwfW_XxlmbxklHs84c/edit?usp=sharing
