#        _______    ______    ______   __    __  _______    ______  
#       |       \  /      \  /      \ |  \  |  \|       \  /      \ 
#       | $$$$$$$\|  $$$$$$\|  $$$$$$\| $$  | $$| $$$$$$$\|  $$$$$$\
#       | $$__/ $$| $$__| $$| $$___\$$| $$__| $$| $$__| $$| $$   \$$
#       | $$    $$| $$    $$ \$$    \ | $$    $$| $$    $$| $$      
#       | $$$$$$$\| $$$$$$$$ _\$$$$$$\| $$$$$$$$| $$$$$$$\| $$   __ 
#    __ | $$__/ $$| $$  | $$|  \__| $$| $$  | $$| $$  | $$| $$__/  \
#   |  \| $$    $$| $$  | $$ \$$    $$| $$  | $$| $$  | $$ \$$    $$
#    \$$ \$$$$$$$  \$$   \$$  \$$$$$$  \$$   \$$ \$$   \$$  \$$$$$$ 
#                                                                   
#                                                                   
#                                                                   

## If not running interactively, don't do anything ##
    case $- in
        *i*) ;;
        *) return;;
    esac

## set variable identifying the chroot you work in (used in the prompt below) ##
    if [ -z "${debian_chroot:-}" ] && [ -r /etc/debian_chroot ]; then

        debian_chroot=$(cat /etc/debian_chroot)

    fi

## make less more friendly for non-text input files, see lesspipe(1) ##
    [ -x /usr/bin/lesspipe ] && eval "$(SHELL=/bin/sh lesspipe)"

## History Customization ##
    HISTCONTROL=ignoredups
    HISTSIZE=10000
    HISTFILESIZE=10000
    shopt -s histappend
    shopt -s checkwinsize

# set a fancy prompt (non-color, unless we know we "want" color) #
    case "$TERM" in
    
        xterm-color|*-256color) color_prompt=yes;;

    esac

    #force_color_prompt=yes

    if [ -n "$force_color_prompt" ]; then
        if [ -x /usr/bin/tput ] && tput setaf 1 >&/dev/null; then

            color_prompt=yes

        else

            color_prompt=

        fi
    fi

## Tab Suggestions, Completions, Aliases and Source Files ##

    ## Aliases
    if [ ! "${EUID:-$(id -u)}" -eq 0 ]; then

        . ~/.dotfiles/.bash_aliases

    elif [ "${EUID:-$(id -u)}" -eq 0 ]; then

        . ~/.bash_aliases

    fi

    ## Git
    if [ ! "${EUID:-$(id -u)}" -eq 0 ]; then

        source ~/.config/git/git-prompt.sh
        source ~/.config/git/git-completion.bash

    elif [ "${EUID:-$(id -u)}" -eq 0 ]; then

        source ~/git-prompt.sh
        source ~/git-completion.bash

    fi

## Custom PS1 ##

    if [ "$color_prompt" = yes ] && [ ! "${EUID:-$(id -u)}" -eq 0 ]; then
        PS1='\
\[\e[0;37m\]\n\[\e[0m\]\
\[\e[1;3;33m\]$(__git_ps1 " שׂ %s")\[\e[0m\]\
\[\e[0;37m\]\n\[\e[0m\]\
${debian_chroot:+($debian_chroot)}\
\[\e[0;1;37m\] >\[\e[0m\]\
\[\e[0;1;37m\]_ \[\e[0m\]\
'
    elif [ "$color_prompt" = yes ] && [ "${EUID:-$(id -u)}" -eq 0 ]; then
        PS1='\
\[\e[0;37m\]\n\[\e[0m\]\
\[\e[1;3;33m\]$(__git_ps1 " שׂ %s")\[\e[0m\]\
\[\e[0;37m\]\n\[\e[0m\]\
${debian_chroot:+($debian_chroot)}\
\[\e[0;1;31m\] >\[\e[0m\]\
\[\e[0;1;31m\]_ \[\e[0m\]\
'
    elif [ "$color_prompt" =  ] && [ "${EUID:-$(id -u)}" -eq 0 ]; then
        PS1='\
\[\e[0;37m\]\n\[\e[0m\]\
\[\e[1;3;33m\]$(__git_ps1 " שׂ %s")\[\e[0m\]\
\[\e[0;37m\]\n\[\e[0m\]\
${debian_chroot:+($debian_chroot)}\
\[\e[0;1;31m\] >\[\e[0m\]\
\[\e[0;1;31m\]_ \[\e[0m\]\
'
    elif [ "$color_prompt" =  ] && [ "${EUID:-$(id -u)}" -eq 0 ]; then
        PS1='\
\[\e[0;37m\]\n\[\e[0m\]\
\[\e[1;3;33m\]$(__git_ps1 " שׂ %s")\[\e[0m\]\
\[\e[0;37m\]\n\[\e[0m\]\
${debian_chroot:+($debian_chroot)}\
\[\e[0;1;31m\] >\[\e[0m\]\
\[\e[0;1;31m\]_ \[\e[0m\]\
'
    fi

    unset color_prompt force_color_prompt

export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This loads nvm bash_completion
