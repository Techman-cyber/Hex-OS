# Changelog

## 0.10.1
- Shortcuts: the shortcut file now contains ALL Xfce default shortcuts (Alt+F4, Alt+Tab, Ctrl+Alt+T, Alt+F2, Print, volume/media keys ...) plus the Windows-style ones.
  Before, the "override" setting made Xfce ignore every default command shortcut. Win+Tab no longer clashes with Xfce's own Super+Tab.
- New "Test the keyboard shortcuts" tool to tell a broken shortcut from a key that Windows/VirtualBox never passed on.

## 0.10
- Task View redesigned: desktops across the top, windows of the chosen desktop below, solid background.
- New Settings app (search, Network, Display, Sound, Accounts, Updates, About ...) and a new Wi-Fi window.
- Quick Settings made compact: hides hardware that is missing, no longer freezes while opening, reads the real theme.
- Start-up loading screen; the chime now plays when the desktop is ready. Logout/restart/shut-down sound. Power menu.
- Less lag: no window compositor by default in virtual machines; calm (static) login screen in virtual machines.
- Removed the taskbar weather text (it showed "(genmon)XXX"); weather stays in the Widgets panel.

## 0.9
- Task View (Win+Tab) with virtual desktops; Windows-style shortcuts (Win+Arrows snapping, Ctrl+Win+Left/Right, Win+V, Win+Shift+S, Win+L, Win+A, Win+D, Win+E).
- Quick Settings panel (Win+A): Wi-Fi, Bluetooth, focus mode, night light, dark mode, animations, volume, brightness, screenshot, wallpaper, lock, power.
- Widgets panel gets a System card (CPU, memory, disk, battery, uptime).
- Sound fix: sound utilities installed, audio is unmuted at login, a "Test the sound" tool explains missing devices.
- Login screen v3: animated background, lock screen with big clock, avatar picker, shake on wrong password, Caps Lock warning, battery.
- Three more wallpapers (sunset, graphite, ocean) and a wallpaper switcher.
- Clipboard history and screen lock (light-locker) included.

## 0.8
- Widgets panel (Win+W): weather (Open-Meteo), calendar and news (RSS); weather text on the taskbar.
- Sounds: startup chime, system event sounds, on/off switch. Boot animation (Plymouth) with progress bar.
- Window fade animations (Smooth mode, works in VMs) and Glass mode (blur) with a chooser in the Welcome app.
- New login screen: big clock, avatar, smoother transitions, password reveal button.
- Wi-Fi support software added (wpasupplicant, iw, rfkill, regulatory data).
- Build now skips packages that do not exist in Debian 12 (with a loud warning) instead of failing.

## 0.7.1
- Build fix: removed `virtualbox-guest-x11` and `virtualbox-guest-utils` from the package list. They do not exist in Debian 12 and stopped the ISO build.

## 0.7
- Windows-style layout: one taskbar at the bottom, Start menu with search (Windows key), smaller icons.
- New HEX login screen with **Create a new account** (admin-approved) and a safe fallback to the standard login screen.
- Preinstalled apps: LibreOffice, Notepad, Paint, VLC, PDF viewer, Task Manager.
- Custom yellow cursor theme (arrow, pointing hand, grab hand, text).
- Removed the Nexora entry from the OS; Firefox is the browser.

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
