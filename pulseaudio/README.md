pulseaudio - audio proxy

[Wiki](https://wiki.archlinux.org/index.php/PulseAudio)
[Docs](https://www.freedesktop.org/wiki/Software/PulseAudio/Documentation/)
[Under the hood](https://gavv.github.io/blog/pulseaudio-under-the-hood/)
[System wide config](https://www.freedesktop.org/wiki/Software/PulseAudio/Documentation/User/SystemWide/)
[Audio setup](https://github.com/alexa-pi/AlexaPi/wiki/Audio-setup-&-debugging#pulseaudio)

### config

* `/etc/pulse/default.pa`

  `
  load-module module-alsa-source device=capture
  load-module module-alsa-sink device=playback
  load-module module-combine-sink
  `

* `/etc/pulse/client.conf`

  `autospawn = no`

### service `/etc/systemd/system/pulseaudio.service`

### load analog device

`
load-module module-alsa-source device=hw:1,0
load-module module-alsa-sink device=hw:0,0
load-module module-combine-sink
`

### other commands

* `chmod -x /usr/bin/start-pulseaudio-x11` - prevent pulse audio from starting on graphical logon

