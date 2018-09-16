### service

`sudo service bluetooth status`
`sudo systemctl start hciuart`

### discover devices

`hcitool scan`

### setup 

`bluetoothctl`

```
[bluetooth]# agent on
Agent registration enabled
[bluetooth]# default-agent
No agent is registered
```

Scanning ...
        28:39:5E:E1:D1:28       [TV] Samsung ...
        D4:A3:3D:2E:5E:F2       Uldis's iPhone

### reset

```
rfkill block bluetooh
rfkill unblock bluetooth
sudo systemctl restart bluetooth
```

### debug

`rfkill list all` - interfaces
`hcitool dev` - bluetooth devices
`lsmod | grep blue` - bluetooth modules
`bluetoothd -v` - bluez version

### more

`bluez-tools` - tools for managing bluez
