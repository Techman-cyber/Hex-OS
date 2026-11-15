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
