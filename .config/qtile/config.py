#     ______  ________  ______  __        ________  
#    /      \|        \|      \|  \      |        \ 
#   |  $$$$$$\\$$$$$$$$ \$$$$$$| $$      | $$$$$$$$ 
#   | $$  | $$  | $$     | $$  | $$      | $$__     
#   | $$  | $$  | $$     | $$  | $$      | $$  \    
#   | $$ _| $$  | $$     | $$  | $$      | $$$$$    
#   | $$/ \ $$  | $$    _| $$_ | $$_____ | $$_____  
#    \$$ $$ $$  | $$   |   $$ \| $$     \| $$     \ 
#     \$$$$$$\   \$$    \$$$$$$ \$$$$$$$$ \$$$$$$$$ 
#         \$$$                                      
#                                                   
#                                                   

import os
import subprocess
from libqtile.lazy import lazy
from colors import colors, icons
from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen

auto_fullscreen = False                 # Prevents a Window to automaticaly set itself to fullscreen when not asked
bring_front_click = False                # Bring a Window to Front When Clicked
cursor_warp = False                     # Cursor Follows window selection, and warps to center
follow_mouse_focus = False              # Mouse Hover to Change Window Focus
focus_on_window_activation = "smart"    # _NET_ACTIVATE_WINDOW Behavior
reconfigure_screens = True              # Automatic Screen Reconfiguration
auto_minimize = True                    # Allow apps to auto-minimize themselves when losing focus
wl_input_rules = None                   # Wayland Input Devices
myTerminal = "alacritty"                # Default Terminal;


#    _  __            ____  _           _ _                 
#   | |/ /           |  _ \(_)         | (_)                
#   | ' / ___ _   _  | |_) |_ _ __   __| |_ _ __   __ _ ___ 
#   |  < / _ \ | | | |  _ <| | '_ \ / _` | | '_ \ / _` / __|
#   | . \  __/ |_| | | |_) | | | | | (_| | | | | | (_| \__ \
#   |_|\_\___|\__, | |____/|_|_| |_|\__,_|_|_| |_|\__, |___/
#              __/ |                               __/ |    
#             |___/                               |___/     

mod = "mod4"                

keys = [
    Key([mod], "i", lazy.layout.up(),
         desc = "Move focus up"
    ),

    Key([mod], "j", lazy.layout.left(),
        desc = "Move focus to left"
    ),

    Key([mod], "k", lazy.layout.down(),
        desc = "Move focus down"
    ),

    Key([mod], "l", lazy.layout.right(),
        desc = "Move focus to right"
    ),

    Key([mod, "shift"], "i", lazy.layout.shuffle_up(),
        desc = "Move window up"
    ),

    Key([mod, "shift"], "j", lazy.layout.swap_left(),
        desc = "Move window to the left"
    ),

    Key([mod, "shift"], "k", lazy.layout.shuffle_down(),
        desc = "Move window down"
    ),

    Key([mod, "shift"], "l", lazy.layout.swap_right(),
        desc = "Move window to the right"
    ),

    Key([mod, "control"], "i", lazy.layout.grow(),
        desc = "Grow window up"
    ),

    Key([mod, "control"], "j", lazy.layout.shrink_main(),
        desc = "Grow window to the left"
    ),

    Key([mod, "control"], "k", lazy.layout.shrink(),
        desc = "Grow window down"
    ),

    Key([mod, "control"], "l", lazy.layout.grow_main(),
        desc = "Grow window to the right"
    ),

    Key([mod], "space", lazy.layout.flip(),
        desc = "Reset all window sizes"
    ),

    Key([mod, "control"], "f", lazy.window.toggle_fullscreen(),
        desc = "Toggle Fullscreen"
    ),

    Key([mod], "r", lazy.layout.reset(),
        desc = "Reset all window sizes"
    ),

    Key([mod], "f", lazy.layout.maximize(),
        desc = "Maximize/Minimize for MonadTall Layout"
    ),

    Key([mod], "v", lazy.window.toggle_floating(),
        desc = "Toggle Floating Layout"
    ),

    Key([mod], "d", lazy.screen.next_group(),
        desc = "Swith to the Next Workspace"
    ),

    Key([mod], "a", lazy.screen.prev_group(),
        desc = "Swith to the Previous Workspace"
    ),

    Key([mod], "c", lazy.window.kill(),
        desc = "Kill Focused Window"
    ),

    Key([mod], "F9", lazy.reload_config(),
        desc = "Reload Qtile Config"
    ),

    Key([mod], "F12", lazy.restart(),
        desc = "Restart Qtile"
    ),

    Key([mod, "control"], "F12", lazy.shutdown(),
        desc = "Shutdown Qtile"
    ),

#                                _ _           _   _                 
#              /\               | (_)         | | (_)                
#             /  \   _ __  _ __ | |_  ___ __ _| |_ _  ___  _ __  ___ 
#            / /\ \ | '_ \| '_ \| | |/ __/ _` | __| |/ _ \| '_ \/ __|
#           / ____ \| |_) | |_) | | | (_| (_| | |_| | (_) | | | \__ \
#          /_/    \_\ .__/| .__/|_|_|\___\__,_|\__|_|\___/|_| |_|___/
#                   | |   | |                                        
#                   |_|   |_|                                        

    Key([mod], "Return", lazy.spawn(myTerminal),
        desc = "Launch terminal"
    ),

    Key([mod, "control"], "c", lazy.spawn("slock"),
        desc = "Lock Screen with slock"
    ),

    Key([mod, "control"], "Return", lazy.spawn("rofi -modi drun,run -show drun"),
        desc = "Launch Rofi"
    ),

    Key([mod], "period", lazy.spawn("rofi -modi emoji -show emoji"),
        desc = "Launch Rofi Emoji"
    ),

    Key([mod], "F1", lazy.spawn("firefox"),
        desc = "Launch Firefox"
    ),

    Key([mod], "F2", lazy.spawn("code"),
        desc = "Launch VSCode"
    ),

    Key([mod], "F3", lazy.spawn("thunar"),
        desc = "Launch File Manager"
    ),

    Key([mod], "F4", lazy.spawn("spotify"),
        desc = "Launch Spotify"
    ),

    Key([mod], "F5", lazy.spawn("steam"),
        desc = "Launch Steam"
    ),

    Key([mod], "F6", lazy.spawn(myTerminal +" -e runrdp"),
        desc = "Launch xfreerdp"
    ),

    Key([mod], "F11", lazy.spawn("xkill"),
        desc = "Launch xkill"
    ),

    Key([mod], "b", lazy.spawn("changebg"),
        desc = "Change Background"
    ),
]

mouse = [
    Drag([mod], "Button3", lazy.window.set_position_floating(), start = lazy.window.get_position(),
        desc = "Set Window to Floating Mode and Move"
    ),

    Drag([mod], "Button1", 
        lazy.window.set_size_floating(), start = lazy.window.get_size(),
        desc = "Resize Floating Window"
    ),

    Click([mod], "Button2", lazy.window.bring_to_front(),
        desc = "Bring Floating Window to Front"
    ),
]

#    ______   _                   _     _                     _                                        _   
#   |  ____| | |                 | |   (_)                   | |                                      | |  
#   | |__    | |   ___     __ _  | |_   _   _ __     __ _    | |        __ _   _   _    ___    _   _  | |_ 
#   |  __|   | |  / _ \   / _` | | __| | | | '_ \   / _` |   | |       / _` | | | | |  / _ \  | | | | | __|
#   | |      | | | (_) | | (_| | | |_  | | | | | | | (_| |   | |____  | (_| | | |_| | | (_) | | |_| | | |_ 
#   |_|      |_|  \___/   \__,_|  \__| |_| |_| |_|  \__, |   |______|  \__,_|  \__, |  \___/   \__,_|  \__|
#                                                    __/ |                      __/ |                      
#                                                   |___/                      |___/                       

floating_layout = layout.Floating(
    float_rules = [
        *layout.Floating.default_float_rules,     # Default Rules;
        Match(wm_class = "confirmreset"),         # gitk;
        Match(wm_class = "makebranch"),           # gitk;
        Match(wm_class = "maketag"),              # gitk;
        Match(wm_class = "ssh-askpass"),          # ssh-askpass;
        Match(title = "branchdialog"),            # gitk;
        Match(title = "pinentry")                 # GPG key password entry;
    ],
    border_focus = colors["00"],        # Focused Floating Window - Boder Color;
    border_normal = colors["00"],       # Unfocused Floating Window - Border Color;
    border_width = 0,                   # Border Width;
    fullscreen_border_width = 0,        # Border Width When in Fullscreen;
    max_border_width = 0                # Maximum Border Width;
)

#    _______   _   _   _                     _                                        _   
#   |__   __| (_) | | (_)                   | |                                      | |  
#      | |     _  | |  _   _ __     __ _    | |        __ _   _   _    ___    _   _  | |_ 
#      | |    | | | | | | | '_ \   / _` |   | |       / _` | | | | |  / _ \  | | | | | __|
#      | |    | | | | | | | | | | | (_| |   | |____  | (_| | | |_| | | (_) | | |_| | | |_ 
#      |_|    |_| |_| |_| |_| |_|  \__, |   |______|  \__,_|  \__, |  \___/   \__,_|  \__|
#                                   __/ |                      __/ |                      
#                                  |___/                      |___/                       

layout_defaults = {
        "border_focus" : colors["02"],      # Focused Window - Border Color;
        "border_normal" : colors["00"],     # Unfocused Window - Border Color;
        "border_width" : 2,                 # Border Width;
        "margin" : 5                        # Margin (Gap);
}

layouts = [
    layout.MonadTall(
        **layout_defaults,
        ratio = 0.6,
        max_ratio = 0.80,
        min_ratio = 0.20,
        min_secondary_size = 85,
        change_ratio = 0.03,
        change_size = 20,
        new_client_position = "bottom",
        single_border_width = 0,
        single_margin = 5
    ),

#    layout.Max(
#        **layout_defaults
#    ),

#    layout.Stack(
#        **layout_defaults
#    ),

#    layout.Bsp(
#        **layout_defaults
#    ),

#    layout.Matrix(
#        **layout_defaults
#    ),

#    layout.MonadWide(
#        **layout_defaults
#    ),

#    layout.RatioTile(
#        **layout_defaults
#    ),

#    layout.Tile(
#        **layout_defaults
#    ),

#    layout.TreeTab(
#        **layout_defaults
#    ),

#    layout.VerticalTile(
#        **layout_defaults
#    ),

#    layout.Zoomy(
#        **layout_defaults
#    ),

#    layout.Columns(
#        **layout_defaults
#    ),
]

#   __          __        _                                  
#   \ \        / /       | |                                 
#    \ \  /\  / /__  _ __| | _____ _ __   __ _  ___ ___  ___ 
#     \ \/  \/ / _ \| '__| |/ / __| '_ \ / _` |/ __/ _ \/ __|
#      \  /\  / (_) | |  |   <\__ \ |_) | (_| | (_|  __/\__ \
#       \/  \/ \___/|_|  |_|\_\___/ .__/ \__,_|\___\___||___/
#                                 | |                        
#                                 |_|                        

groups = [
    Group(
        name = "1",
        label = "󰖟",
        layout = "monadtall"
    ),

    Group(
        name = "2",
        label = "󰆍",
        layout = "monadtall"
    ),

    Group(
        name = "3",
        label = "󰉖",
        layout = "MonadTall"
    ),

    Group(
        name = "4",
        label = "󰓇",
        layout = "MonadTall"
    ),

    Group(
        name = "5",
        label = "󰓓",
        layout = "MonadTall"
    ),

    Group(
        name = "6",
        label = "󰢹",
        layout = "MonadTall"
    ),

#    Group(
#        name = "7",
#        label = " ",
#        layout = "MonadTall"
#    ),

#    Group(
#        name = "8", 
#        label = " ",
#        layout = "MonadTall"
#    ),

#    Group(
#        name = "9", 
#        label = " ",
#        layout = "MonadTall"
#    ),
]

for i in groups:
    keys.extend(
        [
            Key([mod], i.name, lazy.group[i.name].toscreen(),
                desc = "Switch to group {}".format(i.name)
            ),

            Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group = True),
                desc = "Move focused window to group {}".format(i.name)
            ),

            Key([mod, "control"], i.name, lazy.window.togroup(i.name),
                desc = "move focused window to group {}".format(i.name)
            ),
        ]
    )

#    __          ___     _            _       
#    \ \        / (_)   | |          | |      
#     \ \  /\  / / _  __| | __ _  ___| |_ ___ 
#      \ \/  \/ / | |/ _` |/ _` |/ _ \ __/ __|
#       \  /\  /  | | (_| | (_| |  __/ |_\__ \
#        \/  \/   |_|\__,_|\__, |\___|\__|___/
#                           __/ |             
#                          |___/              

widget_defaults = dict(
    background = colors["00"],
    foreground = colors["08"],
    font = "Hack NF Bold",
    fontsize = 12,
    padding = 0
)
extension_defaults = widget_defaults.copy()

qtile_bar_icons = {
    "font" : "Material Design Icons Desktop",
    "background" : colors["00"],
    "fontsize" : 18,
    "padding" : 0
}

qtile_bar_sep = {
    "padding" : 20
}

#    _______    ______   _______    ______  
#   |       \  /      \ |       \  /      \ 
#   | $$$$$$$\|  $$$$$$\| $$$$$$$\|  $$$$$$\
#   | $$__/ $$| $$__| $$| $$__| $$| $$___\$$
#   | $$    $$| $$    $$| $$    $$ \$$    \ 
#   | $$$$$$$\| $$$$$$$$| $$$$$$$\ _\$$$$$$\
#   | $$__/ $$| $$  | $$| $$  | $$|  \__| $$
#   | $$    $$| $$  | $$| $$  | $$ \$$    $$
#    \$$$$$$$  \$$   \$$ \$$   \$$  \$$$$$$ 
#                                           
#                                           
#                                           

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.Sep(
                    padding= 2,
                    foreground = colors["00"]
                ),

#                widget.TextBox(
#                    **qtile_bar_icons,
#                    foreground = colors["05"],
#                    text = icons["arch"],
#                    mouse_callbacks = {"Button1": lazy.spawn("rofi -modi drun,run -show drun")}
#                ),

                widget.GroupBox(
                    font = "Hack NF Regular",
                    active = colors["08"],
                    inactive = colors["08"],
                    block_highlight_text_color = colors["08"],
                    urgent_border = colors["10"],
                    urgent_text = colors["10"],
                    highlight_color = colors["10"],
                    this_current_screen_border = colors["06"],
                    highlight_method = "block",
                    urgent_alert_method = "line",
                    borderwidth = 3,
                    rounded = True,
                    center_aligned = True,
                    disable_drag = True,
                    fontsize = 18,
                    margin = 3,
                    padding = 4
                ),

                widget.WindowName(
                    foreground = colors["00"],
                    for_current_screen = True,
                    format = " {name}",
                    max_chars = 85
                ),

                widget.TextBox(
                    **qtile_bar_icons,
                    foreground = colors["12"],
                    text= icons["volu"],
                    mouse_callbacks = {"Button1": lazy.spawn(myTerminal + " -e pulsemixer")}
                ),

                widget.PulseVolume(
                    foreground = colors["12"],
                    limit_max_volume = True,
                    step = 2,
                    volume_app = "pulsemixer",
                    mouse_callbacks = {"Button1": lazy.spawn(myTerminal + " -e pulsemixer")}
                ),

                widget.Sep(
                    **qtile_bar_sep,
                    foreground = colors["00"]
                ),

                widget.TextBox(
                    **qtile_bar_icons,
                    foreground = colors["02"],
                    text = icons["upda"],
                    mouse_callbacks = {"Button1": lazy.spawn(myTerminal + " -e sudo pacman -Syyu")}
                ),

                widget.CheckUpdates(
                    colour_have_updates = colors["02"],
                    colour_no_updates = colors["02"],
                    no_update_string = "0",
                    distro = 'Arch',
                    display_format = '{updates}',
                    mouse_callbacks = {"Button1": lazy.spawn(myTerminal + " -e sudo pacman -Syyu")}
                ),

                widget.Sep(
                    **qtile_bar_sep,
                    foreground = colors["00"]
                ),

                widget.TextBox(
                    **qtile_bar_icons,
                    foreground = colors["08"],
                    text = icons["cpu"],
                    mouse_callbacks = {"Button1": lazy.spawn(myTerminal + " -e btop")}
                ),

                widget.CPU(
                    format = '{freq_current}GHz {load_percent}%',
                    update_interval = 0.5,
                    foreground = colors["08"],
                    mouse_callbacks = {"Button1": lazy.spawn(myTerminal + " -e btop")}
                ),

                widget.Sep(
                    **qtile_bar_sep,
                    foreground = colors["00"]
                ),

                widget.TextBox(
                    **qtile_bar_icons,
                    foreground = colors["05"],
                    text = icons["gpu"]
                ),

                widget.ThermalSensor(
                    foreground = colors["05"],
                    tag_sensor = "Package id 0"
                ),

                widget.Sep(
                    **qtile_bar_sep,
                    foreground = colors["00"]
                ),

                widget.TextBox(
                    **qtile_bar_icons,
                    foreground = colors["14"],
                    text = icons["mem"],
                    mouse_callbacks = {"Button1": lazy.spawn(myTerminal + " -e htop")}
                ),

                widget.Memory(
                    format = '{MemUsed:.0f}{mm}/{MemTotal:.0f}{mm}',
                    foreground = colors["14"],
                    mouse_callbacks = {"Button1": lazy.spawn(myTerminal + " -e htop")}
                ),

                widget.Sep(
                    **qtile_bar_sep,
                    foreground = colors["00"]
                ),

                widget.TextBox(
                    **qtile_bar_icons,
                    foreground = colors["11"],
                    text = icons["pom"]
                ),

                widget.Pomodoro(
                    color_active = colors["11"],
                    color_inactive = colors["11"],
                    color_break = colors["11"],
                    prefix_active = "",
                    prefix_break = "Take a Break ! ",
                    prefix_long_break = "Take a Break ! ",
                    length_pomodori = 25,
                    length_short_break = 5,
                    length_long_break = 15,
                    prefix_inactive = "25min"
                ),

                widget.Sep(
                    **qtile_bar_sep,
                    foreground = colors["00"]
                ),

                widget.TextBox(
                    **qtile_bar_icons,
                    foreground = colors["04"],
                    text = icons["clo"]
                ),

                widget.Clock(
                    format = "%a %d - %I:%M %p",
                    foreground = colors["04"]
                    #mouse_callbacks= open_calendar
                ),

                widget.Sep(
                    padding=5,
                    foreground = colors["00"],
                    background = colors["00"]
                ),

                widget.Sep(
                    **qtile_bar_sep,
                    foreground = colors["08"]
                ),

                widget.Systray(
                    background = colors["00"],
                    padding = 5
                ),

                widget.Sep(
                    padding= 10,
                    foreground = colors["00"]
                ),

                widget.TextBox(
                    **qtile_bar_icons,
                    foreground = colors["09"],
                    text = icons["aler"],
                    mouse_callbacks = {"Button1": lazy.spawn("dunstctl history-pop")}
                ),

                widget.Sep(
                    padding= 10,
                    foreground = colors["00"]
                ),

#                widget.TextBox(
#                    **qtile_bar_icons,
#                    foreground = colors["09"],
#                    text = icons["wifi"],
#                    mouse_callbacks = {"Button1": lazy.spawn("rofi-wifi-menu")}
#                ),
#
#                widget.Sep(
#                    padding= 10,
#                    foreground = colors["00"]
#                ),

                widget.QuickExit(
                    **qtile_bar_icons,
                    foreground = colors["09"],
                    default_text = icons["shut"],
                    mouse_callbacks = {"Button1": lazy.spawn("exitmenu")}
                ),

                widget.Sep(
                    padding= 10,
                    foreground = colors["00"]
                )
            ],
            size = 32,
            margin = [5, 5, 0, 5],
            background = colors["00"],
        ),
    ),
]

#                  _                    _____ _             _   
#       /\        | |                  / ____| |           | |  
#      /  \  _   _| |_ ___    ______  | (___ | |_ __ _ _ __| |_ 
#     / /\ \| | | | __/ _ \  |______|  \___ \| __/ _` | '__| __|
#    / ____ \ |_| | || (_) |           ____) | || (_| | |  | |_ 
#   /_/    \_\__,_|\__\___/           |_____/ \__\__,_|_|   \__|
#                                                               

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/autostart.sh'])


# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"

# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FRO#eadedaM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
