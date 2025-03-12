# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=auto'
alias grep='grep --color=auto'
PS1='[\u@\h \W]\$ '


# Initialize Pywal
if [[ -f ~/.cache/wal/sequences ]]; then
    (cat ~/.cache/wal/sequences &)
fi

# Source the Pywal colors for the current session
if [[ -f ~/.cache/wal/colors.sh ]]; then
    source ~/.cache/wal/colors.sh
fi
