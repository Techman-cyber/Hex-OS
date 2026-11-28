# Troubleshooting

## Logging in
- **Live session (booting the ISO):** it logs in by itself. If a login screen appears, the account is
  username `user`, password `live`. A live ISO has no other users, so any other name will fail.
- **After installing with the installer:** use the username and password you created in the installer.
  The live account `user` is gone after installing.
- The keyboard layout on the live ISO is US. If your keyboard is different, characters like `@ # " z y`
  may be in other places. Type the password `live` with a US layout in mind.
- Guest login is switched off on purpose. Passwords are never disabled.

## Screen flicker or blinking in VirtualBox
Recommended settings: **Display → Graphics Controller: VMSVGA**, **Video memory: 128 MB**,
**Enable 3D Acceleration: off**, **System → Enable EFI: off**, 4 GB RAM or more.
HEX uses the safe modesetting driver without GL acceleration in virtual machines, and turns blur off there.
VirtualBox Guest Additions are not part of Debian 12, so the screen does not resize by itself in VirtualBox:
set the resolution in **Settings -> Display**, and copy/paste between your PC and the VM is not available.
Blur can be tried from **Welcome → Blur and effects**; switch it off again if it flickers.

## Reporting a problem
Open **Welcome to HEX OS → Troubleshooting report**. It saves `~/hex-diagnose.txt`.
Send that file together with a description of what you saw.

## Accounts, sign up and forgotten passwords
- **Create an account from the login screen:** click **Create a new account**. An administrator must approve it by typing
  their username and password, and the new account is a standard (non-admin) account. In a live session the administrator is `user` / `live`.
- Already logged in? **Welcome to HEX OS -> Create a new account** can also make an administrator account.
- **Forgot the password of an installed system?** Boot the HEX USB, open **Welcome to HEX OS -> Reset a forgotten password**,
  pick the disk and the account, and set a new one. (Encrypted disks are not supported by this tool.)
- If the HEX login screen cannot start, the standard login screen starts instead, so you can always log in.

## Using HEX like Windows
- **Start menu + search:** click the HEX button at the bottom left, or press the Windows key, and type to search.
- **Taskbar:** pinned apps at the bottom left, open windows in the middle, tray and clock at the right. The far-right edge shows the desktop.
- **Win + E** opens Files. Apps included: Firefox, LibreOffice, Notepad, Paint, VLC, Task Manager.

## Why does the live session have an account and admin rights?
A live USB has no accounts yet, so it needs one to log in: `user` / `live`. It has admin rights (no password
for admin tasks) only so the **Install HEX OS** button can start the installer. This exists only in the live
session in memory. An installed HEX OS has **no** `user` account and **no** auto-login: you choose your own
username and password in the installer.

## Wi-Fi
- Wi-Fi works through the network icon in the taskbar tray (or **Welcome -> Wi-Fi and network**). The Wi-Fi support software
  (`wpasupplicant`) and common Wi-Fi firmware are included.
- **In a virtual machine you will only see Ethernet.** VirtualBox and similar programs give the VM a wired adapter and no Wi-Fi.
  Test Wi-Fi on a real computer (USB boot), or give the VM a USB Wi-Fi adapter.

## Weather and news
- Press **Win+W** or click the cloud button on the taskbar. Type your city once. Weather comes from open-meteo.com (free, no account);
  headlines come from BBC World, Hacker News and NASA. Nothing is contacted until you open the panel or set a city.
- Edit the news sources in `~/.config/hex-widgets.json` (the `feeds` list).

## Sounds, animations and boot screen
- **Welcome -> Sounds on / off**, **Welcome -> Animations and effects** (Smooth, Glass, Off).
- The boot animation is a Plymouth theme at `/usr/share/plymouth/themes/hex`.

## Virtual desktops and shortcuts
- **Win+Tab** opens Task View: every window on every desktop. Click a window to jump to it, right-click for "Move to Desktop" or "Close".
  **+ New desktop** adds one. There are 3 desktops by default.
- **Ctrl+Win+Left/Right** switch desktop, **Ctrl+Win+Shift+Left/Right** move the current window with you, **Ctrl+Win+D** new desktop, **Ctrl+Win+F4** close the current one.
- **Win+Left/Right** snap a window to half the screen (or drag it to a screen edge), **Win+Up** maximise, **Win+Down** minimise.
- **Win+V** clipboard history, **Win+Shift+S** screenshot of an area (copied to the clipboard), **Win+L** lock, **Win+A** Quick settings.

## No sound?
- Open **Welcome -> Test the sound**. It plays the chime and tells you what is missing.
- In VirtualBox, audio is off unless you tick **Settings -> Audio -> Enable Audio** (shut the VM down first). Real computers need no setting.
- The speaker icon in the tray opens the mixer; **Quick settings (Win+A)** has a volume slider and mute button.

## Lag, loading screen and logout sound
- **Lag in a virtual machine:** HEX turns window effects off by default inside VMs, because VirtualBox draws them in software.
  Give the VM **4 or more CPU cores**, **4 GB RAM or more**, **128 MB video memory**, and leave **3D acceleration off**.
  **Quick settings -> Animations** (or **Welcome -> Animations and effects**) turns the fade effects on if you want them.
- **Loading screen:** after you log in, a "Starting your desktop..." screen covers the gap, and the start-up chime plays when the desktop actually appears.
- **Logout sound:** it plays when you choose Log out, Restart or Shut down from the Start menu or the power button in Quick settings.

## Settings and Wi-Fi
- **Settings** (the gear on the taskbar) has everything in one place, with a search box.
- **Wi-Fi:** the Wi-Fi window lists networks, shows signal strength and asks for the password. In VirtualBox there is no Wi-Fi adapter to show.
  The VM sees a wired connection (Ethernet), whatever your PC uses. On a real computer your Wi-Fi networks appear automatically.

## Shortcuts like Alt+F4 or Alt+Tab do nothing
1. Open **Welcome -> Test the keyboard shortcuts**, then press the shortcut:
   - the test window **closes** (Alt+F4) or the window **changes** (Alt+Tab): the shortcut works;
   - you **see the key** in the tester but nothing else happens: the key arrived but the desktop ignored it, please report which one;
   - **nothing at all** happens: Windows or VirtualBox kept the key and it never reached HEX.
2. In VirtualBox, click once inside the VM window. Make sure **File -> Preferences -> Input -> Keyboard -> Auto Capture Keyboard**
   is ticked. The **Host key** (Right Ctrl) gives the keyboard back to Windows. Windows-key shortcuts and Alt+Tab are the
   ones a Windows host most often grabs when the VM does not have the keyboard.
3. The shortcut file contains every standard Xfce shortcut plus the Windows-style ones (see `tools/make-shortcuts.py`).
