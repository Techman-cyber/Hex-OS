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

## Forgot your password / need another account
- Linux has no "sign up" button on the login screen. Accounts are made in the installer, or later with
  **Welcome to HEX OS → Create a new account**.
- Forgot the password of an installed system? Boot the HEX USB, open **Welcome to HEX OS → Reset a forgotten
  password**, pick the disk and the account, and set a new password. (Encrypted disks are not supported by this tool.)
- Dock: **Welcome → Show / hide the dock**. It sits on the right side with big icons.
