# HEX OS

A free, good-looking, easy operating system. Based on **Debian 12** with the **Xfce** desktop and **LightDM**.

- **Easy:** normal desktop, normal installer (Calamares), works in virtual machines
- **Crazy looking:** dark Arc theme, generated hex wallpaper, Papirus icons, window shadows and transparency
- **Interactive icons:** HEX Dock, where icons zoom as your mouse gets close
- **Private and safe:** no telemetry added by HEX, firewall (ufw), AppArmor, automatic security updates
- **Recovery:** Timeshift system snapshots
- **Apps:** Firefox, Thunar files, terminal, Synaptic for Debian apps, and Flatpak/Flathub
- **Welcome app:** first-run menu (install, apps, look, shortcuts, snapshots)
- **Local AI (beta):** optional. Downloads a small model that runs on your own computer, only if you ask

## Download
Open the **Releases** page and download `hex-os.iso`. Verify it with `SHA256SUMS.txt`.
(If the ISO is split into `.part` files, see `JOIN-INSTRUCTIONS.txt`.)

## Try it in VirtualBox
1. New machine: Linux, Debian (64-bit), **4 GB RAM**, **25 GB disk**. Leave EFI off at first (simpler).
2. Settings → Display: Graphics Controller **VMSVGA**, video memory **128 MB**, 3D acceleration **off**. (A line about "vmwgfx ... host log message" on boot is a harmless VirtualBox message.)
3. Settings → Storage: choose the ISO. Start.
4. The desktop logs in by itself. The first start applies the HEX look after a few seconds.
5. To install to the disk, double-click **Install HEX OS** on the desktop or in the dock.

Live session login (if a login screen appears): user `user`, password `live`. After installing, use the account you create in the installer. See `TROUBLESHOOTING.md`.

## Build it yourself
On Debian 12: `sudo bash build.sh`. The ISO appears in `out/`.
Or let GitHub build it: Actions → Build HEX OS ISO → Run workflow (add a tag like `v0.2` to publish a release).

## Layout
- `config/package-lists/hex.list.chroot` lists the packages
- `config/includes.chroot/` holds files copied into the OS (wallpaper, setup script, dock, launchers)
- `build.sh` builds the ISO

## License
MIT. Debian and bundled packages keep their own licenses.
