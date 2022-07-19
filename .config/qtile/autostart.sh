#!/usr/bin/env bash

    eval $(/usr/bin/gnome-keyring-daemon --start --components=gpg,pkcs11,secrets,ssh) &
    export GNOME_KEYRING_CONTROL GNOME_KEYRING_PID GPG_AGENT_INFO SSH_AUTH_SOCK &
    xrandr --output DisplayPort-2 --mode 1920x1080 --rate 165 &
    xrandr --output LVDS-1 --mode 1366x768 --rate 60 &
    xset s off -dpms &
    nitrogen --set-zoom-fill --random ~/Media/Pictures/Wallpapers/ &
    picom --experimental-backends --config ~/.config/picom/picom.conf -b &
    dunst -conf/config "$HOME/.config/dunst/dunstrc" &
    lxsession &
    nm-applet &
    volumeicon &
    #cbatticon &
    exec dbus-launch &
