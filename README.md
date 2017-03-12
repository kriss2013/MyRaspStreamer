# MyRaspStreamer
most simple streaming solution. Focus is on absolute ease of use.

# Hardware
Raspberry 3, as ist has WLAN support from the start

# Install 3rd party software

## Solution with mopidy
- mopidy -> streaming daemon
- mpc -> command line client to configure mopidy
- alsa-utils

## solution with volumio 2 (instructions valid for volumio-2.118-2017-03-07-pi)
- volumio -> http://volumio.org. 2 users are created: root and volumio. Both with volumio as password. only volumio can login with ssh
- use the volumio gui to put one radio stream in "My Web Radio" (was http://direct.franceinter.fr/live/franceinter-midfi.mp3)
- put the radio in the playing queue (pull down menu on the right of the radio entry in "My Web Radio" -> "add to queue")
- install cron job in order to stop and restart the radio during the night. All as root (using f.i. sudo)
    - apt-get update && apt-get install -y cron
- reboot in the night
    - sudo crontab -e
    - 0 3 * * * /sbin/init 6        
full path to init is necesary, otherwise the job will not run
