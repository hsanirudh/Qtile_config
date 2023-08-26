## Requirements : psutil,scrot,rofi,FuraCode_NerdFont(any),firefox
## Do chmod +x autostart.sh
## Enter your username in line 62

## Imports ##
import os
import subprocess
from libqtile import qtile
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.command import lazy
from libqtile import layout, bar, widget, hook
from libqtile.lazy import lazy
from typing import List  # noqa: F401 

## My defaults ##
mod = "mod1" # It is "alt"{change to mod4 if you want super as mod key}
browser = "firefox"
myTerminal = "alacritty"

## Key Bindings ##
keys = [
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(myTerminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    # Toggle Apps
    Key([mod], "b", lazy.spawn(browser), desc="Launch_Browser"),
    Key([mod], "space", lazy.spawn("rofi -show drun"), desc="Launch_rofi"),
    # Volume
    Key([], 'XF86AudioMute', lazy.spawn('pactl set-sink-mute @DEFAULT_SINK@ toggle')),
    Key([], 'XF86AudioLowerVolume', lazy.spawn('pulseaudio-ctl down +5%')),
    Key([], 'XF86AudioRaiseVolume', lazy.spawn('pulseaudio-ctl up +5%')),
    # Brightness
    Key([], 'XF86MonBrightnessUp', lazy.spawn('brightnessctl set +5%')),
    Key([], 'XF86MonBrightnessDown', lazy.spawn('brightnessctl set 5%-')),
    # ScreenShot
    Key([mod], "Print", lazy.spawn("scrot /home/<username>/Screenshots/%Y-%m-%d-%T-screenshot.png"))
]

## GroupBox ##

groups = [Group("", layout='monadtall'),
          Group("", layout='monadtall'),
          Group("", layout='monadtall'),
          Group("", layout='monadtall'),
          Group("", layout='monadtall'),
          Group("", layout='monadtall'),
          Group("", layout='monadtall'),
          Group("", layout='monadtall'),
          Group("", layout='monadtall')]

from libqtile.dgroups import simple_key_binder
dgroups_key_binder = simple_key_binder(mod)

## Mouse_callback functions

# Shutdown
def shutdown_now():
  qtile.cmd_spawn('shutdown now')
# Reboot
def reboot_now():
  qtile.cmd_spawn('reboot')
# Open_htop
def open_htop():
  qtile.cmd_spawn(myTerminal + ' -e htop')
# Speedtest.net
def speedtest():
  qtile.cmd_spawn(browser + 'www.speedtest.net')
# Brightness Up 
def brightup():
  qtile.cmd_spawn('brightnessctl set +5%')
# Brightness Down
def brightdown():
  qtile.cmd_spawn('brightnessctl set 5%-')

# Colors ##

colors = [["#2f3541", "#2f3541"],
          ["#ffffff", "#ffffff"],
          ["#d56d77", "#d56d77"],
          ["#ffb480", "#ffb480"],
          ["#fce43c", "#fce43c"],  
          ["#42d6a4", "#42d6a4"],
          ["#08cad1", "#08cad1"],
          ["#59adf6", "#59adf6"],
          ["#8abec6", "#8abec6"],
          ["#ff5722", "#ff5722"],
          ["#d323ac", "#d323ac"]]

## Widget Defaults ##
widget_defaults = dict(
    background=colors[0]
)

extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
              widget.Spacer(
                length = 6,
                background = colors[0],
                ),                
              widget.GroupBox(
                fontsize = 20,
                margin_x = 1,
                margin_y = 4,
                padding_y = 0,
                padding_x = 1,
                borderwidth = 2.5,
                active = colors[2],
                inactive = colors[1],
                rounded = True,
                highlight_color = colors[0],
                highlight_method = "line",
                this_current_screen_border = colors[8],
                this_screen_border = colors [0],
                foreground = colors[2],
                center_aligned = True,
                disable_drag = True,
                background = colors[0]
                ),
              widget.Systray(
                background = colors[0],
                icon_size = 16,
                foreground = colors[1],
                padding = 3),
              widget.Spacer(
                background = colors[0],
                ),
              widget.TextBox(
                text='',
                background = colors[0],
                foreground = colors[2],
                fontsize = 12,
                mouse_callbacks = {'Button1': brightup, 'Button3': brightdown},
                padding = 0
                ),
              widget.Backlight(
                background = colors[0],
                foreground = colors[2],
                backlight_name = 'intel_backlight',
                brightness_file = 'brightness',
                fontsize = 11
                ),
              widget.TextBox(
                text='',
                background = colors[0],
                foreground = colors[8],
                fontsize = 35,
                padding = 2
                ),
              widget.TextBox(
                text='',
                foreground = colors[2],
                background = colors[0],
                fontsize = 22,
                padding = 0
                ),
              widget.PulseVolume(
                background = colors[0],
                foreground = colors[2],
                limit_max_volume = True,
                padding_y = 1,
                fontsize = 11
                ),
              widget.TextBox(
                text='',
                background = colors[0],
                foreground = colors[8],
                fontsize = 35,
                padding = 2
                ),
              widget.TextBox(
                text='',
                background = colors[0],
                foreground = colors[2],
                fontsize = 17,
                padding = 1,
                mouse_callbacks = {'Button1': open_htop},
                ),
              widget.Memory(
                background = colors[0],
                foreground = colors[2],
                format = '{MemUsed: .0f}{mm}/{MemTotal: .0f}{mm}',
                padding = 0,
                fontsize = 11
                ),
              widget.TextBox(
                text='',
                background = colors[0],
                foreground = colors[8],
                fontsize = 35,
                padding = 2
                ),
              widget.TextBox(
                text='↓↑',
                foreground = colors[2],
                background = colors[0],
                fontsize = 12,
                padding = 0,
                mouse_callbacks={'Button3': speedtest}
                ),
              widget.Net(
                background = colors[0],
                format = '{down} {up}',
                foreground = colors[2],
                fontsize = 12
                ),  
              widget.TextBox(
                text='',
                background = colors[0],
                foreground = colors[8],
                fontsize = 35,
                padding = 2
                ),
              widget.TextBox(
                text='',
                background = colors[0],
                foreground = colors[2],
                fontsize = 27,
                padding = 0,
                ),
              widget.Battery(
                background = colors[0],
                foreground = colors[2],
                format = '{percent:2.0%}',
                full_char = "100%",
                update_interval = 1,
                fontsize = 12,
                ),
              widget.TextBox(
                text='',
                background = colors[0],
                foreground = colors[8],
                fontsize = 35,
                padding = 2
                ),
             widget.TextBox(
                text='',
                foreground = colors[2],
                background = colors[0],
                fontsize = 12,
                padding = 1,
                ),
             widget.Clock(
                format='%d-%m-%Y %a %I:%M:%S %p',
                foreground = colors[2],
                background = colors[0],
                fontsize = 12,
                ),
             widget.TextBox(
                text='',
                background = colors[0],
                foreground = colors[8],
                fontsize = 35,
                padding = 2
                ),
             widget.TextBox(
                text='',
                foreground = colors[2],
                background = colors[0],
                fontsize = 20,
                padding = 1,
                mouse_callbacks = {'Button1': shutdown_now, 'Button3': reboot_now},
                ),
             widget.Spacer(
                length = 6,
                background = colors[0],
                ),                
            ],
            25,
            margin = [0,0,0,0],
        ),
    ),
]

## Layout Themes ##
layout_theme = {"border_width": 1,
                "margin": 6,
                "border_focus": "89bdc5",
                "border_normal": "d56d77"
                }

## Layouts ##

layouts = [
    layout.Floating(**layout_theme),
    layout.MonadTall(**layout_theme),
    layout.Max(**layout_theme),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
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

## Autostart ##
@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.call([home])

wmname = "LG3D" 
