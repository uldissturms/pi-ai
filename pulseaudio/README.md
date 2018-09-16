pulseaudio - audio proxy

[Wiki](https://wiki.archlinux.org/index.php/PulseAudio)
[Docs](https://www.freedesktop.org/wiki/Software/PulseAudio/Documentation/)
[Under the hood](https://gavv.github.io/blog/pulseaudio-under-the-hood/)

## config (`/etc/pulse/default.pa`)

### Load analog device
load-module module-alsa-sink device=hw:0,0
load-module module-combine-sink
