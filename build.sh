#!/usr/bin/env bash
set -euo pipefail

[ "$EUID" -eq 0 ] || exec sudo bash "$0" "$@"

HERE="$(cd "$(dirname "$0")" && pwd)"
export DEBIAN_FRONTEND=noninteractive

apt-get update
apt-get install -y --no-install-recommends \
  live-build \
  debootstrap \
  squashfs-tools \
  xorriso \
  ca-certificates \
  git

rm -rf "$HERE/build" "$HERE/out"
mkdir -p "$HERE/build" "$HERE/out"
cd "$HERE/build"

lb config \
  --distribution bookworm \
  --architectures amd64 \
  --archive-areas "main contrib non-free non-free-firmware" \
  --binary-images iso-hybrid \
  --debian-installer none \
  --apt-recommends false \
  --memtest none \
  --win32-loader false \
  --chroot-squashfs-compression-type xz \
  --iso-application "HEX OS" \
  --iso-publisher "HEX OS" \
  --iso-volume "HEX_OS" \
  --bootappend-live "boot=live components quiet hostname=hex"

cp -a "$HERE/config/." config/
chmod -R a+rX config
chmod 755 config/includes.chroot/usr/local/bin/* config/hooks/normal/* 2>/dev/null || true

lb build 2>&1 | tee "$HERE/build/build.log"

ISO="$HERE/out/hex-os.iso"
mv live-image-amd64.hybrid.iso "$ISO"
ls -lh "$ISO"
echo "Done: $ISO"
