#
# ~/.bash_profile
#

# Custom ".bashrc" dir.

if [ ! "${EUID:-$(id -u)}" -eq 0 ]; then

    . ~/.dotfiles/.bashrc
    export PATH=$PATH:~/.bin/

elif [ "${EUID:-$(id -u)}" -eq 0 ]; then

    . ~/bashrc

fi
