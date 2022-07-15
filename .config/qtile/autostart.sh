#!/usr/bin/env bash

# Set Monitor Resolution and Refresh Rate (xrandr)
    xrandr --output DisplayPort-2 --mode 1920x1080 --rate 165 &
    xrandr --output LVDS-1 --mode 1366x768 --rate 60 &

# Disable Monitor Power Management (xrandr)
    xset s off -dpms &

# Set Wallpaper (Nitrogen)
    nitrogen --set-zoom-fill --random ~/Media/Pictures/Wallpapers/ &

# Start Picom (Compositor)
    picom --experimental-backends --config ~/.config/picom/picom.conf -b &

# Notifications (Dunst)
    dunst -conf/config "$HOME/.config/dunst/dunstrc" &

# Policie Kit (Polkit)
    lxsession &

# Network Applet
    nm-applet &

# Volume Icon Applet
    volumeicon &

# Vscode thing...
    # init keyring
    eval $(/usr/bin/gnome-keyring-daemon --start --components=gpg,pkcs11,secrets,ssh) &
    # export keyring
    export GNOME_KEYRING_CONTROL GNOME_KEYRING_PID GPG_AGENT_INFO SSH_AUTH_SOCK &

    ...

    exec dbus-launch
