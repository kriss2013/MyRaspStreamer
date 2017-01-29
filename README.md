# MyRaspStreamer
most simple streaming solution. Focus is on absolute ease of use.

# Hardware
Raspberry 3, as ist has WLAN support from the start

# Install 3rd party software

## Solution with mopidy
- mopidy -> streaming daemon
- mpc -> command line client to configure mopidy
- alsa-utils

## solution with volumio 2
- volumio -> http://volumio.org. 2 users are created: root and volumio. Both with volumio as password. only volumio can login with ssh
- install cron job in order to stop and restart the radio during the night. All as root (using f.i. sudo)

    apt-get update && apt-get install -y cron
