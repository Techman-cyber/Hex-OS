#!/usr/bin/env python3
"""Builds the HEX keyboard shortcut file: ALL Xfce default shortcuts (so Alt+F4, Alt+Tab, Ctrl+Alt+T ... keep working)
plus the Windows-style HEX ones. Needs Xfce's default file (package libxfce4ui-common).
Run from the project root:  python3 tools/make-shortcuts.py"""
import copy, xml.etree.ElementTree as ET
SYS = "/etc/xdg/xfce4/xfconf/xfce-perchannel-xml/xfce4-keyboard-shortcuts.xml"
OUT = "config/includes.chroot/etc/skel/.config/xfce4/xfconf/xfce-perchannel-xml/xfce4-keyboard-shortcuts.xml"

def prop(name, value=None, typ="string"):
    e = ET.Element("property", {"name": name, "type": typ})
    if value is not None: e.set("value", value)
    return e

src = ET.parse(SYS).getroot()
out = ET.Element("channel", {"name": "xfce4-keyboard-shortcuts", "version": "1.0"})

REPLACE = {  # defaults we change
    "<Alt>F1": "xfce4-popup-whiskermenu",
    "<Primary><Alt>t": "xfce4-terminal",
}
DROP = {"<Alt><Super>s"}          # needs a screen reader that is not installed
ADD_COMMANDS = {
    "Super_L": "xfce4-popup-whiskermenu",
    "<Super>Tab": "bash /usr/local/bin/hex-taskview-toggle",
    "<Super>w": "bash /usr/local/bin/hex-widgets-toggle",
    "<Super>a": "bash /usr/local/bin/hex-quick-toggle",
    "<Super>v": "xfce4-popup-clipman",
    "<Super>l": "xflock4",
    "<Super><Shift>s": "xfce4-screenshooter -r -c",
}
ADD_XFWM = {
    "<Primary><Super>Left": "left_workspace_key",
    "<Primary><Super>Right": "right_workspace_key",
    "<Primary><Super><Shift>Left": "move_window_left_workspace_key",
    "<Primary><Super><Shift>Right": "move_window_right_workspace_key",
    "<Primary><Super>d": "add_workspace_key",
    "<Primary><Super>F4": "del_workspace_key",
    "<Super>Left": "tile_left_key",
    "<Super>Right": "tile_right_key",
    "<Super>Up": "maximize_window_key",
    "<Super>Down": "hide_window_key",
    "<Super>d": "show_desktop_key",
}
for provider in ("commands", "xfwm4"):
    node = ET.SubElement(out, "property", {"name": provider, "type": "empty"})
    custom = ET.SubElement(node, "property", {"name": "custom", "type": "empty"})
    custom.append(prop("override", "true", "bool"))
    default = src.find("./property[@name='%s']/property[@name='default']" % provider)
    for p in default:
        n = p.get("name")
        if n in DROP: continue
        if provider == "xfwm4" and n == "<Super>Tab":
            custom.append(prop(n, None, "empty"))      # Win+Tab is HEX Task View, not Xfce's own switcher
            continue
        q = copy.deepcopy(p)
        if provider == "commands" and n in REPLACE: q.set("value", REPLACE[n])
        custom.append(q)
    extra = ADD_COMMANDS if provider == "commands" else ADD_XFWM
    existing = {c.get("name"): c for c in custom}
    for k, v in extra.items():
        if k in existing: existing[k].set("value", v); existing[k].set("type", "string")
        else: custom.append(prop(k, v))
ET.indent(out)
ET.ElementTree(out).write(OUT, encoding="UTF-8", xml_declaration=True)
print("written", OUT, "->", sum(1 for _ in out.iter("property")), "properties")
