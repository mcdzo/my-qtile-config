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
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
import os
import subprocess
from spotify import Spotify

mod = 'mod4'

terminal = "tilix"  # guess_terminal()

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.Popen([home])

# Colors for the bar


def init_colors():
    return [["#2e3440", "#2e3440"],  # color 0  dark grayish blue
            ["#2e3440", "#2e3440"],  # color 1  dark grayish blue
            ["#3b4252", "#3b4252"],  # color 2  very dark grayish blue
            ["#434c5e", "#434c5e"],  # color 3  very dark grayish blue
            ["#4c566a", "#4c566a"],  # color 4  very dark grayish blue
            ["#d8dee9", "#d8dee9"],  # color 5  grayish blue
            ["#e5e9f0", "#e5e9f0"],  # color 6  light grayish blue
            ["#eceff4", "#eceff4"],  # color 7  light grayish blue
            ["#8fbcbb", "#8fbcbb"],  # color 8  grayish cyan
            ["#88c0d0", "#88c0d0"],  # color 9  desaturated cyan
            ["#81a1c1", "#81a1c1"],  # color 10 desaturated blue
            ["#5e81ac", "#5e81ac"],  # color 11 dark moderate blue
            ["#bf616a", "#bf616a"],  # color 12 slightly desaturated red
            ["#d08770", "#d08770"],  # color 13 desaturated red
            ["#ebcb8b", "#ebcb8b"],  # color 14 soft orange
            ["#a3be8c", "#a3be8c"],  # color 15 desaturated green
            ["#b48ead", "#b48ead"], # color 16 grayish magenta
            ["#1a53ff"] # color 17 blue
            ]  


colors = init_colors()


keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "j", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "k", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "i", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "Tab", lazy.layout.next(),
        desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "j", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "i", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "j", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, "control"], "k", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "i", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "q", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    # Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    # Apps
    Key([mod], "r", lazy.spawn("rofi -show drun")),
    Key([mod], "g", lazy.spawn("google-chrome-stable")),
    Key([mod], "c", lazy.spawn("code")),
    Key([mod], "d", lazy.spawn("discord")),
    Key([mod], "t", lazy.spawn("thunar")),

    # Volume

    Key([], "XF86AudioLowerVolume", lazy.spawn(
        "pactl set-sink-volume @DEFAULT_SINK@ -5%")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn(
        "pactl set-sink-volume @DEFAULT_SINK@ +5%")),
    Key([], "XF86AudioMute", lazy.spawn(
        "pactl set-sink-mute @DEFAULT_SINK@ toggle")),

    # Brightness
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-")),

    # Screenshot
    Key([mod], "s", lazy.spawn("xfce4-screenshooter")),


]

groups = [Group(i) for i in "1234"]

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(
                    i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

layouts = [
    layout.Columns(border_focus=colors[14],  # "#26ed0c"
                   border_normal=colors[4], border_width=3, margin=7, margin_on_single=20, border_on_single=False),
    layout.Max(margin=20, border=colors[10]),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]


widget_defaults = dict(
    font="Cascadia Mono",
    fontsize=12,
    padding=3,
    background=colors[1],
    foreground="#fff",
    border_color=colors[4],
    border_width=2
)

extension_defaults = widget_defaults.copy()
screens = [
    Screen(
        top=bar.Bar(
            [
                #widget.CurrentLayout(),
                widget.GroupBox(
                    active=colors[10],  # b48ead
                    borderwidth=2,
                    disable_drag=True,
                    fontsize=14,
                    hide_unused=False,
                    highlight_method='line',
                    inactive=colors[4],  # e5e9f0
                    margin_x=0,
                    margin_y=3,
                    padding_x=5,
                    padding_y=8,
                    rounded=False,
                    this_current_screen_border=colors[10],  # ebcb8b
                    urgent_alert_method='line'
                ),
                widget.Prompt(),
                widget.WindowName(),
                Spotify(),
                
                widget.Systray(padding=10),
                widget.Sep(
                    background=colors[1],
                    foreground=colors[5],
                    linewidth=5,
                    padding=10,
                    size_percent=50
                ),
                

                # widget.Chord(
                #     chords_colors={
                #         "launch": ("#ff0000", "#ffffff"),
                #     },
                #     name_transform=lambda name: name.upper(),
                # ),

                # widget.TextBox("default config", name="default"),
                # widget.TextBox("Press &lt;M-r&gt; to spawn", foreground="#d75f5f"),
                # NB Systray is incompatible with Wayland, consider using StatusNotifier instead
                # widget.StatusNotifier(),

                # widget.Spacer(),
                # widget.Net(
                #     background=colors[1],
                #     fontsize=12,
                #     foreground=colors[5],
                #     format='{interface}: {down} ↓ ',
                #     interface='wlan0',
                #     padding=0
                # ),
                widget.Wlan(),
                widget.Sep(
                    background=colors[1],
                    foreground=colors[5],
                    linewidth=5,
                    padding=10,
                    size_percent=50
                ),
                widget.Battery(
                    fmt='Battery: {}',
                    padding=5
                ),
                widget.Sep(
                    background=colors[1],
                    foreground=colors[5],
                    linewidth=5,
                    padding=10,
                    size_percent=50
                ),
                widget.PulseVolume(fmt='Vol: {}'),

                widget.Sep(
                    background=colors[1],
                    foreground=colors[5],
                    linewidth=5,
                    padding=10,
                    size_percent=50
                ),
                widget.Backlight(backlight_name="intel_backlight",
                                 backlight_file="/sys/class/backlight/intel_backlight", fmt='Brightness: {}'),
                widget.Sep(
                    background=colors[1],
                    foreground=colors[5],
                    linewidth=5,
                    padding=10,
                    size_percent=50
                ),

                widget.Clock(format="%Y-%m-%d %a %I:%M %p", foreground=colors[14]),
                widget.QuickExit(),


            ],
            28,
            opacity=0.7,


        ),

    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button1", lazy.window.toggle_fullscreen()),
    #Key([mod], "Button1", lazy.window.toggle_fullscreen())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "mcdzo"

autostart = [
    "feh --bg-fill .config/qtile/wallpaper.jpg",
    "picom &"
]

for x in autostart:
    os.system(x)
