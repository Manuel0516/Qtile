from libqtile import bar
from .widgets import *
from libqtile.config import Screen
import os

import time
import threading
import psutil 

def battery_icon():
    battery = psutil.sensors_battery() 
    result = ""
    charge = ""

    if battery.power_plugged == True:
        charge = " "
    
    if battery.percent <= 10:
        result = " "
    elif battery.percent < 20:
        result = " "
    elif battery.percent < 50:
        result = " "
    elif battery.percent < 70:
        result = " "
    elif battery.percent > 80:
        result = " "

    return result + charge

def batt_icon():
    while True:
        return battery_icon()
        time.sleep(60)

screens = [
    Screen(
        top=bar.Bar(
            [   widget.Sep(padding=3, linewidth=0, background="#18101D"),
                widget.Image(filename='~/.config/qtile/planet.png', margin=2, background="#18101D", mouse_callbacks={'Button1': lambda: qtile.cmd_spawn("rofi -show combi")}),
                widget.Sep(padding=4, linewidth=0, background="#18101D"), 
                widget.GroupBox(
                                highlight_method='line',
                                this_screen_border="#5294e2",
                                this_current_screen_border="#5294e2",
                                active="#ffffff",
                                inactive="#848e96",
                                background="#18101D"),
                widget.TextBox(
                       text = '',
                       padding = 0,
                       fontsize = 28,
                       foreground='#18101D'
                       ),    
                widget.Prompt(),
                widget.Spacer(length=5),
                widget.WindowName(fontsize=16, foreground='#fcfcfc',fmt='{}', max_chars=59),
                widget.Chord(
                    chords_colors={
                        'launch': ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget.CurrentLayoutIcon(scale=0.75),
                widget.CheckUpdates(
                    update_interval=1800,
                    distro="Arch_yay",
                    display_format="{updates} Updates",
                    foreground="#ffffff",
                    mouse_callbacks={
                        'Button1':
                        lambda: qtile.cmd_spawn(terminal + ' -e yay -Syu')
                    }),
                widget.TextBox(
                       text = '',
                       padding = 0,
                       fontsize = 28,
                       foreground='#18101D'
                       ), 
                volume,
                widget.TextBox(                                                                    
                       text = '',
                       padding = 0,
                       fontsize = 28,
                       foreground='#18101D',
                       ),
                widget.Battery(
                    padding=5, 
                    format = '{percent:2.0%} {hour:d}:{min:02d} {watt:.2f} W'
                ),
                widget.TextBox(
                    text = batt_icon(),
                    padding = 5,
                    fontsize  = 20
                ),
                widget.TextBox(
                       text = '',
                       padding = 0,
                       fontsize = 28,
                       foreground='#18101D'
                       ),    
                widget.Clock(format=' %Y-%m-%d %a %H:%M',
                             background="#18101D"),
                             
                widget.TextBox(                                                                                
                       text = '',
                       padding = 0,
                       fontsize = 28,
                       foreground='#18101D',
                       ),   
                widget.TextBox(
                    text=' ',
                    mouse_callbacks= {
                        'Button1':
                        lambda: qtile.cmd_spawn(os.path.expanduser('~/.config/rofi/powermenu.sh'))
                    }
                )
                
            ],
            30,  # height in px
            background="#443731"  # background color
        ), ),

Screen(
        top=bar.Bar(
            [   widget.Sep(padding=3, linewidth=0, background="#18101D"),
                widget.Image(filename='~/.config/qtile/planet.png', margin=2, background="#18101D", mouse_callbacks={'Button1': lambda: qtile.cmd_spawn("rofi -show combi")}),
                widget.Sep(padding=4, linewidth=0, background="#18101D"), 
                widget.GroupBox(
                                highlight_method='line',
                                this_screen_border="#5294e2",
                                this_current_screen_border="#5294e2",
                                active="#ffffff",
                                inactive="#848e96",
                                background="#18101D"),
                widget.TextBox(
                       text = '',
                       padding = 0,
                       fontsize = 28,
                       foreground='#18101D'
                       ),    
                widget.Prompt(),
                widget.Spacer(length=5),
                widget.WindowName(fontsize=16, foreground='#fcfcfc',fmt='{}', max_chars=59),
                widget.Chord(
                    chords_colors={
                        'launch': ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget.CurrentLayoutIcon(scale=0.75),
                widget.CheckUpdates(
                    update_interval=1800,
                    distro="Arch_yay",
                    display_format="{updates} Updates",
                    foreground="#ffffff",
                    mouse_callbacks={
                        'Button1':
                        lambda: qtile.cmd_spawn(terminal + ' -e yay -Syu')
                    }),
                widget.TextBox(
                       text = '',
                       padding = 0,
                       fontsize = 28,
                       foreground='#18101D'
                       ), 
                volume,
                widget.TextBox(                                                                    
                       text = '',
                       padding = 0,
                       fontsize = 28,
                       foreground='#18101D',
                       ),
                widget.Battery(
                    padding=5, 
                    format = '{percent:2.0%} {hour:d}:{min:02d} {watt:.2f} W'
                ),
                widget.TextBox(
                    text = batt_icon(),
                    padding = 5,
                    fontsize  = 20
                ),
                widget.TextBox(
                       text = '',
                       padding = 0,
                       fontsize = 28,
                       foreground='#18101D'
                       ),    
                widget.Clock(format=' %Y-%m-%d %a %H:%M',
                             background="#18101D"),
                             
                widget.TextBox(                                                                                
                       text = '',
                       padding = 0,
                       fontsize = 28,
                       foreground='#18101D',
                       ),   
                widget.TextBox(
                    text=' ',
                    mouse_callbacks= {
                        'Button1':
                        lambda: qtile.cmd_spawn(os.path.expanduser('~/.config/rofi/powermenu.sh'))
                    }
                )
                
            ],
            30,  # height in px
            background="#443731"  # background color
        ))
]


