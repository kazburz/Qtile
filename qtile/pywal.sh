#!/bin/bash

wal -i /home/kazbur/.config/qtile/wallpapers/lofi/lofiorange -n --backend colorthief
feh --bg-fill "$(< "${HOME}/.cache/wal/wal")"  
