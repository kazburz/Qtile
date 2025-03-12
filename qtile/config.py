from libqtile import bar, layout, qtile, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

mod = "mod1"
terminal = guess_terminal()

#  -- Key Bindings ------------------------------------------------
keys = [
    # Applications
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "a", lazy.spawn("firefox"), desc="Launch firefox"),
    Key([mod], "s", lazy.spawn("code"), desc="Launch vscode"),
    Key([mod], "d", lazy.spawn("dmenu"), desc="Launch dmenu"),
    Key([mod], "p", lazy.spawn("/home/kazbur/.config/qtile/pywal.sh"), desc="pywal"),


    Key([mod], "f", lazy.window.toggle_floating(), desc="Toggle floating on the focused window"),
    Key([mod], "w", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod], "tab", lazy.window.toggle_fullscreen(), desc="Toggle fullscreen on the focused window"),

    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),

    # Switch between windows
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

    # Multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(), desc="Toggle between split and unsplit sides of stack"),
]

#  -- Mouse Bindings ------------------------------------------------
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

#  -- Groups ------------------------------------------------
groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.extend([
        # mod + group number = switch to group
        Key([mod], i.name, lazy.group[i.name].toscreen(), desc=f"Switch to group {i.name}"),
        # mod + shift + group number = switch to & move focused window to group
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True), desc=f"Switch to & move focused window to group {i.name}"),
    ])

#  -- Layouts ------------------------------------------------
layouts = [
    layout.Columns(border_focus_stack=["#ffffff", "#000000"], border_width=4, margin=10),
    layout.Max(border_focus_stack=["#ffffff", "#000000"], border_width=4, margin=10),
    # Try more layouts by uncommenting below layouts.
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

#  -- Widgets and Screens ------------------------------------------------
widget_defaults = dict(
    font="sans",
    fontsize=12,
    padding=3,
    foreground="#ffffff",
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.CurrentLayout(),
                widget.GroupBox(),
                widget.Prompt(),
                widget.WindowName(),
                widget.Chord(
                    chords_colors={
                        "launch": ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget.TextBox("default config", name="default"),
                widget.TextBox("Press <M-r> to spawn", foreground="#d75f5f"),
                widget.Systray(),
                widget.Clock(format="%Y-%m-%d %a %I:%M %p"),
                widget.QuickExit(),
            ],
            24,
            background="#000000",  
            border_width=[2, 2, 2, 2],  
            border_color="#ffffff", 
        ),
    ),
]

#  -- Other Configurations ------------------------------------------------
dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
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
auto_minimize = True

#  -- Wayland Specific Settings ------------------------------------------------
wl_input_rules = None
wl_xcursor_theme = None
wl_xcursor_size = 24

#  -- Set the Window Manager Name ------------------------------------------------
wmname = "LG3D"

#  -- Virtual Terminal Switching ------------------------------------------------
for vt in range(1, 8):
    keys.append(
        Key(
            ["control", "mod1"],
            f"f{vt}",
            lazy.core.change_vt(vt).when(func=lambda: qtile.core.name == "wayland"),
            desc=f"Switch to VT{vt}",
        )
    )
