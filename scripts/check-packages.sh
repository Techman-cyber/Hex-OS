#!/usr/bin/env bash
# Fails fast (about a minute) if any package name is wrong, before the long build.
set -u
HERE="$(cd "$(dirname "$0")/.." && pwd)"
echo "deb http://deb.debian.org/debian bookworm main contrib non-free non-free-firmware" > /etc/apt/sources.list.d/hex-check.list
apt-get update -qq
bad=0
while read -r p; do
  case "$p" in ""|\#*) continue ;; esac
  apt-cache show "$p" >/dev/null 2>&1 || { echo "MISSING: $p"; bad=1; }
done < "$HERE/config/package-lists/hex.list.chroot"
[ "$bad" = 0 ] && echo "All packages found." || { echo "Fix the MISSING names above."; exit 1; }
