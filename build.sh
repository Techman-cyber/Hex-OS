#!/usr/bin/env bash
# HEX OS build script. Needs Debian 12 (or a Debian 12 container/VM). Run: sudo bash build.sh
set -euo pipefail
[ "$EUID" -eq 0 ] || exec sudo bash "$0" "$@"
HERE="$(cd "$(dirname "$0")" && pwd)"
apt-get update && apt-get install -y live-build debootstrap squashfs-tools xorriso ca-certificates
rm -rf "$HERE/build" && mkdir -p "$HERE/build" "$HERE/out" && cd "$HERE/build"
lb config \
  --distribution bookworm --architectures amd64 \
  --archive-areas "main contrib non-free non-free-firmware" \
  --binary-images iso-hybrid --debian-installer none \
  --apt-recommends false --memtest none --win32-loader false \
  --chroot-squashfs-compression-type xz \
  --iso-application "HEX OS" --iso-publisher "HEX OS" --iso-volume "HEX_OS" \
  --bootappend-live "boot=live components quiet hostname=hex username=user locales=en_US.UTF-8 keyboard-layouts=us timezone=UTC"
cp -a "$HERE/config/." config/
chmod -R a+rX config
chmod 755 config/includes.chroot/usr/local/bin/* config/includes.chroot/usr/local/sbin/* config/hooks/normal/* 2>/dev/null || true
lb build
ISO="$HERE/out/hex-os.iso"
mv live-image-amd64.hybrid.iso "$ISO"
ls -lh "$ISO"
echo "Done: $ISO"
