[AirPlay speakers](https://makezine.com/projects/raspberry-pi-airplay-speaker/)

### install libs

`sudo apt-get install git libao-dev libssl-dev libcrypt-openssl-rsa-perl libio-socket-inet6-perl libwww-perl avahi-utils libmodule-build-perl`

### clone & install SDP

```
git clone https://github.com/njh/perl-net-sdp.git`
perl Build.PL
sudo ./Build
sudo ./Build test
sudo ./Build install
```

### clone & setup receiver

```
git clone https://github.com/hendrikw82/shairport.git
cd shairport
make
```

### start receiver

`./shairport.pl -a [name]`
