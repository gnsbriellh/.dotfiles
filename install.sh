#!/bin/bash

## Home ##

    # .config
        if [  ! -d "$HOME/.config" ]; then
            mkdir -v ~/.config
        fi

    # .bin
        if [ -d "$HOME/.local/.bin" ]; then
            rm -r ~/.local/.bin
        fi
        ln -sfnv $PWD/.bin ~/.local/.bin

    # Bash
        if [ -d "$HOME/.bashrc" ]; then
            rm ~/.bashrc
        fi
        ln -sfnv $PWD/.bash_profile ~/.bash_profile

    # Git
        if [ -d "$HOME/.gitconfig" ]; then
            rm ~/.gitconfig
        fi
        ln -sfnv $PWD/.gitconfig ~/.gitconfig

## .config ##

    # alacritty
        if [ -d "$HOME/.config/alacritty" ]; then
            rm -r ~/.config/alacritty
        fi
        ln -sfnv $PWD/.config/alacritty ~/.config/alacritty

    # btop
        if [ -d "$HOME/.config/btop" ]; then
            rm -r ~/.config/btop
        fi
        ln -sfnv $PWD/.config/btop ~/.config/btop

    # dunst
        if [ -d "$HOME/.config/dunst" ]; then
            rm -r ~/.config/dunst
        fi
        ln -sfnv $PWD/.config/dunst ~/.config/dunst

    # git
        if [ -d "$HOME/.config/git" ]; then
            rm -r ~/.config/git
        fi
        ln -sfnv $PWD/.config/git ~/.config/git

    # picom
        if [ -d "$HOME/.config/picom" ]; then
            rm -r ~/.config/picom
        fi
        ln -sfnv $PWD/.config/picom ~/.config/picom

    # qtile
        if [ -d "$HOME/.config/qtile" ]; then
            rm -r ~/.config/qtile
        fi
        ln -sfnv $PWD/.config/qtile ~/.config/qtile

    # rofi
        if [ -d "$HOME/.config/rofi" ]; then
            rm -r ~/.config/rofi
        fi
        ln -sfnv $PWD/.config/rofi ~/.config/rofi

    # kvantum
        if [ -d "$HOME/.config/Kvantum" ]; then
            rm -r ~/.config/Kvantum
        fi
        ln -sfnv $PWD/.config/Kvantum ~/.config/Kvantum

    # flameshot
        if [ -d "$HOME/.config/flameshot" ]; then
            rm -r ~/.config/flameshot
        fi
        ln -sfnv $PWD/.config/flameshot ~/.config/flameshot
    
    # volumeicon
        if [ -d "$HOME/.config/volumeicon" ]; then
            rm -r ~/.config/volumeicon
        fi
        ln -sfnv $PWD/.config/volumeicon ~/.config/volumeicon

    # VSCode
        ln -sfnv $PWD/.config/Code/User/settings.json ~/.config/Code/User/settings.json
        ln -sfnv $PWD/.config/Code/User/keybindings.json ~/.config/Code/User/keybindings.json

    # Thunar
        if [  ! -d "$HOME/.config/xfce4/xfconf/xfce-perchannel-xml" ]; then
            mkdir -v ~/$HOME/.config/xfce4/xfconf/xfce-perchannel-xml
        fi
        ln -sfnv $PWD/.config/Thunar/uca.xml ~/.config/Thunar/uca.xml
        ln -sfnv $PWD/.config/xfce4/xfconf/xfce-perchannel-xml/thunar.xml ~/.config/xfce4/xfconf/xfce-perchannel-xml/thunar.xml

## ROOT ##

    ROOT_FOLDER="/root"

    # Bash
        if [ -d "$ROOT_FOLDER/.bashrc" ]; then
            sudo rm /root/.bashrc
        fi

        if [ -d "$ROOT_FOLDER/.bash_profile" ]; then
            sudo rm /root/.bash_profile
        fi
        sudo cp -v ~/.dotfiles/.bashrc /root/
        sudo cp -v ~/.dotfiles/.bash_profile /root/
        sudo cp -v ~/.dotfiles/.bash_aliases /root/
        sudo cp -v ~/.dotfiles/.config/git/git-prompt.sh /root/
        sudo cp -v ~/.dotfiles/.config/git/git-completion.bash /root/
