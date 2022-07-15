#!/bin/bash

## Home ##

    # .bin
        if [ -d "$HOME/.bin" ]; then
            rm -r ~/.bin
        fi
        mkdir ~/.bin
        ln -sfnv $PWD/.bin/* ~/.bin/

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

    # VSCode
        ln -sfnv $PWD/.config/Code/User/settings.json ~/.config/Code/User/settings.json
        ln -sfnv $PWD/.config/Code/User/keybindings.json ~/.config/Code/User/keybindings.json

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
