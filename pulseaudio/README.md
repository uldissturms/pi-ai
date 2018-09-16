pulseaudio - audio proxy

[Wiki](https://wiki.archlinux.org/index.php/PulseAudio)

## config (`/etc/pulse/default.pa`)

### Load analog device
load-module module-alsa-sink device=hw:0,0
load-module module-combine-sink
