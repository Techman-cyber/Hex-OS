#!/usr/bin/env bash
# Advisory check (never blocks the build): asks apt if every package name in the list can be found.
# The real judge is the ISO build itself; this just gives an early hint in about a minute.
HERE="$(cd "$(dirname "$0")/.." && pwd)"
S=/etc/apt/sources.list.d/debian.sources
if [ -f "$S" ]; then
  sed -i 's/^Components: main$/Components: main contrib non-free non-free-firmware/' "$S"
else
  echo "deb http://deb.debian.org/debian bookworm main contrib non-free non-free-firmware" > /etc/apt/sources.list.d/hex-check.list
fi
for i in 1 2 3; do apt-get update -qq && break; echo "apt-get update failed, retry $i"; sleep 5; done
PKGS=$(grep -v '^\s*#' "$HERE/config/package-lists/hex.list.chroot" | grep -v '^\s*$' | tr '\n' ' ')
OUT=$(apt-get install -s --no-install-recommends $PKGS 2>&1)
if echo "$OUT" | grep -q '^E:'; then
  echo "Hint: apt reported problems (the build may still work, this check can be wrong):"
  echo "$OUT" | grep '^E:'
else
  echo "All required packages resolve."
fi
exit 0
