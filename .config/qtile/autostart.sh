#!/usr/bin/env bash

    eval $(/usr/bin/gnome-keyring-daemon --start --components=gpg,pkcs11,secrets,ssh)   &   # Init keyring
    export GNOME_KEYRING_CONTROL GNOME_KEYRING_PID GPG_AGENT_INFO SSH_AUTH_SOCK         &   # Export keyring
    xrandr --output DisplayPort-2 --mode 1920x1080 --rate 165                           &   # Set monitor resolution and refresh rate
    xrandr --output LVDS-1 --mode 1366x768 --rate 60                                    &   # Set monitor resolution and refresh rate
    xset s off -dpms                                                                    &   # Disable screen saving
    nitrogen --set-zoom-fill --random ~/Media/Pictures/Wallpapers/                      &   # Set a random background
    picom --experimental-backends --config ~/.config/picom/picom.conf -b                &   # Start picom (Compositor)
    dunst -conf/config "$HOME/.config/dunst/dunstrc"                                    &   # Start dunst (Notifications)
    lxsession                                                                           &   # Start lxsession (polkit)
    flameshot                                                                           &   # Start flameshot (Screenshot tool)
    volumeicon                                                                          &   # Start volumeicon (Manage Volume)
    nm-applet                                                                           &   # Start nm-applet (Network Manager Applet)
    #cbatticon                                                                           &   # Start cbatticon (Battery Status Applet)
