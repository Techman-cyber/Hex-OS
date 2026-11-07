# HEX OS

A free, good-looking, easy operating system. Based on **Debian 12** with **KDE Plasma**.

- **Easy:** normal desktop, normal installer (Calamares), works in virtual machines
- **Crazy looking:** dark neon theme, generated hex wallpaper, Papirus icons, blur, wobbly windows, magic-lamp minimize, window overview
- **Interactive icons:** HEX Dock, where icons zoom as your mouse gets close
- **Private:** no telemetry
- **Apps:** Firefox, Dolphin files, Konsole terminal; install more from the terminal with `sudo apt install <name>`

## Download
Open the **Releases** page and download `hex-os-*.iso`. Verify it with `SHA256SUMS.txt`.
(If the ISO is split into `.part` files, see `JOIN-INSTRUCTIONS.txt`.)

## Try it in VirtualBox
1. New machine: Linux, Debian (64-bit), **4 GB RAM**, **25 GB disk**.
2. Settings → Display: Graphics Controller **VMSVGA**, video memory **128 MB**, 3D acceleration **off** (try on later).
3. Settings → Storage: choose the ISO. Start.
4. The desktop logs in by itself. The first start applies the HEX look after a few seconds.
5. To install to the disk, double-click **Install HEX OS** on the desktop or in the dock.

Live session login (if asked): user `user`, password `live`.

## Build it yourself
On Debian 12: `sudo bash build.sh`. The ISO appears in `out/`.
Or let GitHub build it: Actions → Build HEX OS ISO → Run workflow (add a tag like `v0.2` to publish a release).

## Layout
- `config/package-lists/hex.list.chroot` lists the packages
- `config/includes.chroot/` holds files copied into the OS (wallpaper, setup script, dock, launchers)
- `build.sh` builds the ISO

## License
MIT. Debian and bundled packages keep their own licenses.
