# ------------------------------------------------------------------ #
# ------------------------------------------------------------------ #
#      ___   _    _  _          ____                __  _            #
#     / _ \ | |_ (_)| |  ___   / ___| ___   _ __   / _|(_)  __ _     #
#    | | | || __|| || | / _ \ | |    / _ \ | '_ \ | |_ | | / _` |    #
#    | |_| || |_ | || ||  __/ | |___| (_) || | | ||  _|| || (_| |    #
#     \__\_\ \__||_||_| \___|  \____|\___/ |_| |_||_|  |_| \__, |    #
#                                                          |___/     #
# ------------------------------------------------------------------ #
# ------------------------------------------------------------------ #
# Author: @GoodBoyNeon                                    ---------- #
# ------------------------------------------------------------------ #
# ------------------------------------------------------------------ #


import os
import subprocess

from libqtile import bar, hook, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy

mod = "mod4"

terminal = "alacritty"
web_browser = "firefox"
primary_launcher = "rofi -show run"
secondary_launcher = "dmenu_run"

catppuccin = {
    "rosewater": "#f5e0dc",
    "flamingo": "#f2cdcd",
    "pink": "#f5c2e7",
    "mauve": "#cba6f7",
    "red": "#f38ba8",
    "maroon": "#eba0ac",
    "peach": "#fab387",
    "yellow": "#f9e2af",
    "green": "#a6e3a1",
    "teal": "#94e2d5",
    "sky": "#89dceb",
    "sapphire": "#74c7ec",
    "blue": "#89b4fa",
    "lavender": "#b4befe",
    "text": "#cdd6f4",
    "subtext1": "#bac2de",
    "subtext0": "#a6adc8",
    "overlay2": "#9399b2",
    "overlay1": "#7f849c",
    "overlay0": "#6c7086",
    "surface2": "#585b70",
    "surface1": "#45475a",
    "surface0": "#313244",
    "base": "#1e1e2e",
    "mantle": "#181925",
    "crust": "#11111b"
}

flavor = "mauve"

keys = [
    # Open terminal
    Key([mod], "Return", lazy.spawn(terminal), desc="Lauch terminal"),

    # Launch discord
    Key([mod], "d", lazy.spawn("discord"), desc="Launch Discord"),

    # Qtile actions
    Key([mod, "shift"], "r", lazy.restart(), desc="Restart qtile"),
    Key([mod, "shift"], "x", lazy.shutdown(), desc="Shutdown qtile"),

    # Window actions
    Key([mod], "f", lazy.window.toggle_maximize(), desc="Maximize the window"),

    Key([mod, "shift"], "f", lazy.window.toggle_fullscreen(),
        desc="Toggle full screen"),


    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod, "shift"], "space", lazy.layout.next(), desc="Move window focus to other window"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    Key([mod], "space", lazy.spawn(primary_launcher), desc = "launch my main launcher"),
    Key([mod], "p", lazy.spawn(secondary_launcher), desc = "launch my alternative launcher"),

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

    Key([mod], "w", lazy.spawn(web_browser), desc = "Launch web browser"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
]

groups = []
# group_names = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
# group_names = ['1', '2', '3', '4', '5', '6', '7']
group_names = ['1', '2', '3', '4', '5']

# group_labels = ["WWW", "DEV", "SYS", "DOC", "CHAT", "REC", "GFX", "CONF", "MUS"]
# group_labels =["", "", "", "", "阮", "", "", "", ""] 
# group_labels = ["", "", "", "", "", "", "", "", ""]
# group_labels = ["", "", "", "", "", "", "", "", ""]
# group_labels = ["", "", "", "", "", "", "", "", ""]
group_labels = ["", "", "", "", ""]
# group_labels = ["", "", "", "", "", "", ""]
# group_labels = [1, 2, 3, 4, 5, 6, 7, 8, 9 ]

group_layout = [
    'monadtall',
    'monadtall',
    'monadtall',
    'monadtall',
    'floating',
    'monadtall',
    'monadtall',
    'monadtall',
    'monadtall',
    'monadtall',
]

for i in range(len(group_names)):
    groups.append(
        Group(
            name=group_names[i],
            layout=group_layout[i],
            label=group_labels[i]
        )
    )

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
            # mod1 + shift + letter of group = switch to & move focused window
            # to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )


def init_monad_layout_conf():
    return {
        "border_focus": catppuccin[flavor],
        "border_normal": catppuccin['base'],
        # "margin": 28,
        "margin": 8,
        "border_width": 2,
    }

layout_conf = init_monad_layout_conf()

layouts = [
    layout.MonadTall(**layout_conf),
    layout.Floating(**layout_conf),
    layout.MonadWide(**layout_conf),
    layout.Columns(**layout_conf),
    layout.Max(**layout_conf),
    layout.Stack(**layout_conf),
    layout.Bsp(**layout_conf),
    layout.Matrix(**layout_conf),
    layout.RatioTile(**layout_conf),
    layout.Tile(**layout_conf),
    layout.TreeTab(**layout_conf),
    layout.VerticalTile(**layout_conf),
    layout.Zoomy(**layout_conf),
    layout.Spiral(**layout_conf),
]


### BAR CONFIGURATION ###

# Variables

# default_font = "JetBrainsMono Nerd Font"
# default_font = "RobotoMono Nerd Font"
# default_font = "Roboto Medium"
default_font = "Ubuntu SemiBold"

nerdfont = "JetBrainsMono Nerd Font"

widget_defaults = dict(
    font=default_font,
    fontsize=16,
    padding=2,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.Spacer(
                    length=20,
                ),
                widget.GroupBox(
                    font=nerdfont,
                    fontsize=18,
                    margin_x=5,
                    margin_y=3,
                    border_width=0,
                    active=catppuccin["red"],
                    inactive=catppuccin[flavor],
                    rounded=True,
                    highlight_method="text",
                    this_current_screen_border=catppuccin["green"],
                ),
                widget.Spacer(
                    length=bar.STRETCH,
                ),
                widget.Spacer(
                    length=16,
                ),
                widget.Volume(
                    font=nerdfont,
                    fmt="墳",
                    foreground=catppuccin['blue'],
                ),
                widget.Volume(
                    fmt=" {}",
                    foreground=catppuccin['blue'],
                    mute_command="pamixer -t",
                ),
                widget.Spacer(
                    length=16,
                ),
                widget.TextBox(
                    font=nerdfont,
                    text="",
                    foreground=catppuccin["red"],
                ),
                widget.CPU(
                    format=" {load_percent:04}%",
                    foreground=catppuccin["red"],
                ),
                widget.Spacer(
                    length=16
                ),
                ### UPDATES SECTION START ###
                widget.TextBox(
                    font=nerdfont,
                    text="ﮮ",
                    foreground=catppuccin["green"],
                ),
                widget.CheckUpdates(
                    format=' {}',
                    foreground=catppuccin['green'],
                    colour_have_updates=catppuccin['green'],
                    colour_no_updates=catppuccin['green'],
                    padding=5,
                    distro='Arch_checkupdates',
                    initial_text="loading...",
                    execute=terminal + " -e sudo pacman -Syu --noconfirm",
                    # mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(terminal + ' -e sudo pacman -Syu')},
                    update_interval=60,
                    no_update_string='0',
                ),
                widget.TextBox(
                    text=" |",
                    foreground=catppuccin['green']
                ),
                widget.CheckUpdates( format=' {}', foreground=catppuccin['green'],
                    colour_have_updates=catppuccin['green'],
                    colour_no_updates=catppuccin['green'],
                    padding=5,
                    distro='Arch_yay',
                    initial_text="loading...",
                    execute=terminal + " -e yay -Syu --noconfirm",
                    update_interval=60,
                    no_update_string='0',
                ),
                ### UPDATES SECTION END ###
                widget.Spacer(
                    length=30,
                ),
                widget.Spacer(
                    length=10,
                    background=catppuccin["surface0"],
                ),
                widget.Systray(
                    icon_size=20,
                    padding=0,
                    background=catppuccin["surface0"]
                ),
                widget.Spacer(
                    length=10,
                    background=catppuccin["surface0"],
                ),
                widget.Spacer(
                    length=20,
                ),
                widget.TextBox(
                    font=nerdfont,
                    foreground=catppuccin['flamingo'],
                    text=' ',
                ),
                widget.Clock(
                    # font="Roboto, Regular",
                    format='%y-%m-%d',
                    foreground=catppuccin['flamingo'],
                ),
                widget.Spacer(
                    length=10,
                ),
                widget.TextBox(
                    font=nerdfont,
                    text=' ',
                    foreground=catppuccin['yellow'],
                ),
                widget.Clock(
                    format='%H:%M',
                    foreground=catppuccin['yellow'],
                ),
                widget.Spacer(
                    length=10,
                ),
                widget.CurrentLayoutIcon(
                    custom_icon_paths=[os.path.expanduser("~/.config/qtile/layouts/")],
                    scale=0.6,
                    padding=0,
                ),
                widget.Spacer(
                    length=10,
                ),
            ],
            28,
            # margin=[12, 12, 4, 12],
            background=catppuccin["base"],
            border=catppuccin[flavor]
        ),
    ),
]


# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
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
# auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

### HOOKS ###

# startup apps
@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.run([home])

@hook.subscribe.client_new
def func(c):
    if c.name == "alacritty":
        c.togroup(3)

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
