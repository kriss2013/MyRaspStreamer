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
- volumio -> http://volumio.org
- install cron job in order to stop and restart the radio during the night
    apt-get update && apt-get install -y cron
