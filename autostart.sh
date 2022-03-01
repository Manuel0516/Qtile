#!/bin/sh
feh --bg-scale /usr/share/endeavouros/backgrounds/wallpaper2.jpg
picom & disown # --experimental-backends --vsync should prevent screen tearing on most setups if needed

# Start welcome
#eos-welcome & disown

/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 & disown # start polkit agent from GNOME

#Config monitors
bash /home/manuel/.config/qtile/screen.sh &
