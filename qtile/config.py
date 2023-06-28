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

from libqtile import bar, layout, widget, extension, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
### Python imports ###
from os import path

mod = "mod4"
alt = "mod1"
terminal = guess_terminal()

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    # Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    ## Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    ## Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    ## Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    ## Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
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
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    # Custom keys
    Key([mod], "u", lazy.group["Home"].toscreen(), desc="Switch group Home to active screen"),
    Key([mod, "shift"], "u", lazy.window.togroup("Home", switch_group=True), desc="Switch window & screen to group Home"), 
    Key([mod], "i", lazy.group["Media"].toscreen(), desc="Switch group Media to active screen"),
    Key([mod, "shift"], "i", lazy.window.togroup("Media", switch_group=True), desc="Switch window & screen to group Media"),
    Key([mod], "o", lazy.group["Dev"].toscreen(), desc="Switch group Dev to active screen"),
    Key([mod, "shift"], "o", lazy.window.togroup("Dev", switch_group=True), desc="Switch window & screen to group Dev"), 
    Key([mod], "p", lazy.group["Audit/etc"].toscreen(), desc="Switch group Audit/etc to active screen"),
    Key([mod, "shift"], "p", lazy.window.togroup("Audit/etc", switch_group=True), desc="Switch window & screen to group Audit/etc"), 
    Key([mod], "z", lazy.window.toggle_minimize(), desc="Toggle minimization"),
    Key([mod], "f", lazy.window.toggle_floating(), desc="Toggle Windows floating"),
    Key([mod], "space", lazy.group.next_window(), desc="Move window focus to the next window"),
    Key([mod, "shift"], "space", lazy.group.prev_window(), desc="Move window focus to the previous window"),
    Key([mod], "m", lazy.spawn("/home/timmyt/.config/rofi/launchers/type-1/launcher.sh"), desc="Spawns rofi"),
    ### Default (if not using adi1090x rofi themes
    ### Key([mod], "m", lazy.spawn("rofi -show combi"), desc="Spawns rofi"),
    # Key([mod], "m", lazy.run_extension(extension.DmenuRun(
    #     dmenu_bottom = True,
    #     # dmenu_height=24,
    #     # dmenu_lines=13,
    #     dmenu_prompt="<|>",
    #     font="Hack",
    #     fontsize=16,
    #     background="#240f36",
    #     foreground="#d900ff",
    #     selected_background="#4e2984",
    #     selected_foreground="#00ff03",
    # ))),
    Key([mod, "control"], "h", lazy.layout.shrink_main(), desc="Shrink main window"),
    Key([mod, "control"], "l", lazy.layout.grow_main(), desc="Grow the main window"),
    Key([mod, "control"], "k", lazy.layout.grow(), desc="Grow window"),
    Key([mod, "control"], "j", lazy.layout.shrink(), desc="Shrink window"),
    Key([mod, alt], "space", lazy.widget["keyboardlayout"].next_keyboard(), desc="Next keyboard layout."),
    Key([mod], "e", lazy.spawn("doublecmd"), desc="File explorer spawner"),
]
# Nerd fonts required for labels
# Check https://www.nerdfonts.com/#home for more info
groups = [
    Group(
        name="Home",
        label=""
    ),
    Group(
        name="Media",
        label="󰐌",
        matches=[
            Match(wm_class=["spotify", "Spotify"])
        ]
    ),
    Group(
        name="Dev",
        label="",
        matches=[
            Match(wm_class=["code", "Code"])
        ]
    ),
    Group(
        name="Audit/etc",
        label=""
    )
]

# groups = [Group(i) for i in "123456789"]

# for i in groups:
#     keys.extend(
#         [
#            # mod1 + letter of group = switch to group
#             Key(
#                 [mod],
#                 i.name,
#                 lazy.group[i.name].toscreen(),
#                 desc="Switch to group {}".format(i.name),
#             ),
#             # mod1 + shift + letter of group = switch to & move focused window to group
#             Key(
#                 [mod, "shift"],
#                 i.name,
#                 lazy.window.togroup(i.name, switch_group=True),
#                 desc="Switch to & move focused window to group {}".format(i.name),
#             ),
#             # Or, use below if you prefer not to switch to that group.
#             # # mod1 + shift + letter of group = move focused window to group
#             # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
#             #     desc="move focused window to group {}".format(i.name)),
#         ]
#     )

layouts = [
    # layout.Columns(
    #     border_focus="#00BCE1",
    #     border_normal="#1E22AA",
    #     grow_amount=5,
    #     # border_focus_stack=["#d75f5f", "#8f3d3d"],
    #     # border_width=2,
    #     margin=3,
    # ),
    layout.MonadTall(
        margin=5,
        ratio=0.7,
        single_border_width=0,
        border_focus="#00BCE1",
        border_normal="#1E22AA"
    ),
    layout.Max(margin=5),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font="fredoka one",
    fontsize=14,
    padding_x=5,
)
extension_defaults = widget_defaults.copy()

primaryBar = bar.Bar(
            size=35,
            background="#240f36",
            margin=[5, 5, 0, 5],
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
            widgets=[
                ### Left
                widget.CurrentLayoutIcon(
                    custom_icon_paths=[
                        path.join(path.expanduser("~"), ".config/qtile/LayoutIcons"),
                    ],
                    background="#8af5f9",
                    # padding is necessary to avoid bugs
                    padding=0,
                    scale=0.6,
                ),
                # widget.CurrentLayout(),
                widget.GroupBox(
                    # highlight_method="text",
                    highlight_method="line",
                    background="#000",
                    active="#fff",
                    fontsize=23,
                    inactive="#404040",
                    this_current_screen_border="#00BCE1",
                    this_screen_border="#1E22AA",
                    other_current_screen_border="#00BCE1",
                    other_screen_border="#1E22AA",
                    padding=0,
                    disable_drag=True,
                ),
                widget.Memory(
                    background="#1b041a",
                    foreground="#FB48C4",
                ),
                widget.TextBox(
                    text="󰋊",
                    fontsize=40,
                    padding=5,
                    background="#0f0c28",
                    foreground="#5ffee9"
                ),
                widget.DF(
                    background="#0f0c28",
                    foreground="#5ffee9",
                    visible_on_warn = False,
                    warn_color = "#E0E722",
                    warn_space = 50,
                    padding=8,
                    format='{p}  {r:.0f}%|{uf}{m}'
                ),
                widget.WindowCount(
                    show_zero = False,
                    background="#065170",
                    foreground="#fbfcfb",
                    mouse_callbacks = {
                        "Button1": lazy.group.next_window(),
                        "Button3": lazy.group.prev_window(),
                        # "Click": lazy.group.next_window(),
                    },
                ),
                ### Mid
                widget.Spacer(),
                widget.Prompt(),
                widget.WindowName(),
                widget.Spacer(),
                ### Right
                widget.Chord(
                    chords_colors={
                        "launch": ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                # widget.TextBox("default config", name="default"),
                # widget.TextBox("Press &lt;M-r&gt; to spawn", foreground="#d75f5f"),
                # NB Systray is incompatible with Wayland, consider using StatusNotifier instead
                # widget.StatusNotifier(),
                widget.Systray(
                    icon_size=22,
                    padding=15
                ),
                widget.KeyboardLayout(
                    padding=10,
                    configured_keyboards=["us", "es"]
                ),
                widget.Net(
                    background="#1b041a",
                    foreground="#FB48C4",
                ),
                widget.Clock(
                    background="#000",
                    format="%d-%m-%Y %A %H:%M:%S"
                ),
                widget.WidgetBox(
                    background="#8af5f9",
                    foreground="#000",
                    close_button_location="right",
                    text_closed="  ",
                    text_open="  ",
                    fontsize=30,
                    widgets=[
                        widget.LaunchBar(
                            background="#8af5f9",
                            foreground="#000",
                            text_only=True,
                            fontsize=25,
                            progs=[
                                ("", "reboot", "Reboot"),
                                ("", "shutdown now", "Shutdown"),
                            ]
                        )
                    ]
                ),
                # widget.QuickExit(),
            ],
)

# Check http://docs.qtile.org/en/latest/manual/faq.html#how-can-i-match-the-bar-with-picom
# @hook.subscribe.startup
# def _():
#         primaryBar.window.window.set_property("QTILE_BAR", 1, "CARDINAL", 32)

secondaryBar=bar.Bar(
        size=35,
        background="#721D77",
        widgets=[
            widget.CurrentLayout(),
        ],
)

# fake_screens = [
#     Screen(
#         x = 0,
#         y = 0,
#         width = 1920,
#         height = 1080,
#     ),
#     Screen(
#         top = customBar,
#         x = 1920,
#         y = 0,
#         width = 1920,
#         height = 1080,
#     ),
# ]

screens = [
    Screen(
        top = primaryBar,
    ),
    Screen(
        top = secondaryBar,
        # A custom gap
        # bottom=bar.Gap(10)
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
# Default Option
# follow_mouse_focus = True
# Custom option
follow_mouse_focus = False
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
wmname = "LG3D"
