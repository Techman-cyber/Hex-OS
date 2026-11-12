# Changelog

## 0.4
- Login: the live account (`user` / `live`) is now created and unlocked on every live boot, and auto-login is generated only in the live session (it used to be a fixed file that would also end up in installed systems). Guest login off.
- Flicker: virtual GPUs (VirtualBox, QEMU, VMware) use the kernel modesetting driver without GL acceleration; the VMware X driver was removed; the dock no longer restarts at first login; vsync off for the window manager in VMs.
- Blur: blurred login screen everywhere; desktop blur (picom) automatic on real hardware, optional in VMs from the Welcome app.
- Glass-style top panel, rounded GTK controls; new troubleshooting report.

## 0.3
- Switched desktop from KDE Plasma to Xfce + LightDM (the Plasma session showed a black screen in VirtualBox)
- Added VirtualBox/QEMU guest packages and X11 fallback drivers
- Welcome app and AI beta now use Zenity

## 0.2
- New base: Debian 12 + KDE Plasma (X11), replacing the Arch/Hyprland prototype
- HEX Dock (Plank) with zoom, generated wallpaper, HEX color scheme, window effects
- Calamares graphical installer
- Firewall (ufw), AppArmor, automatic security updates, Timeshift snapshots
- Discover software store with Flathub
- Welcome app and optional local AI (beta)
