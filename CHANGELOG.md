# Changelog

## 0.6
- Removed the Plank dock (it duplicated, clipped and blocked full screen). The slim Xfce dock panel is now on the right edge, auto-hides, and has small icons.
- Cleaner top bar (no workspace block), new modern wallpaper and login background.
- Nexora is the browser entry (dock, menu, default web handler); Firefox is the engine behind it until Nexora has a Linux build.
- Login screen hints: live credentials, forgot password, how to create another account.

## 0.5
- Simpler, bigger UI: larger fonts, desktop icons, panel and terminal; the dock is now big, always visible, on the right side, with no zoom or auto-hide (it clipped and glitched in VMs).
- Login screen shows the live credentials (user / live) in a live session, and a "forgot your password?" hint on installed systems.
- New tools: "Reset a forgotten password" (run from the live USB) and "Create a new account", both in the Welcome app and the Applications menu.

## 0.4.1
- Removed Synaptic (its dependency `debtags` broke the live-build package install). "Get apps" is now a small built-in installer for Debian (apt) and Flathub apps.
- Build failures now show the error lines first, plus free disk space, in the run's annotation.

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
