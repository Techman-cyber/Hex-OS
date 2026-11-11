#!/usr/bin/env bash
set -euo pipefail

if [ "${EUID:-$(id -u)}" -ne 0 ]; then
  exec sudo bash "$0" "$@"
fi

HERE="$(cd "$(dirname "$0")" && pwd)"

apt-get update
DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
  live-build \
  debootstrap \
  squashfs-tools \
  xorriso \
  ca-certificates

rm -rf "$HERE/build" "$HERE/out"
mkdir -p "$HERE/build" "$HERE/out"

cd "$HERE/build"

LB_ARGS=(
  --distribution bookworm
  --architectures amd64
  --archive-areas "main contrib non-free non-free-firmware"
  --binary-images iso-hybrid
  --debian-installer none
  --apt-recommends false
  --memtest none
  --win32-loader false
  --iso-application "HEX OS"
  --iso-publisher "HEX OS"
  --iso-volume "HEX_OS"
  --bootappend-live "boot=live components quiet hostname=hex"
)

# Some live-build versions do not support this flag.
if lb --help 2>&1 | grep -q -- '--chroot-squashfs-compression-type'; then
  LB_ARGS+=(--chroot-squashfs-compression-type xz)
fi

lb config "${LB_ARGS[@]}"

cp -a "$HERE/config/." config/
chmod -R a+rX config
find config/includes.chroot/usr/local/bin config/hooks/normal -type f -exec chmod 755 {} + 2>/dev/null || true

lb build

ISO="$HERE/out/hex-os.iso"
mv live-image-amd64.hybrid.iso "$ISO"
ls -lh "$ISO"
echo "Done: $ISO"
