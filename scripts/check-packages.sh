#!/usr/bin/env bash
# Check package names in the configured Debian Bookworm repositories.
set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PACKAGE_LIST="$HERE/config/package-lists/hex.list.chroot"
APT_SOURCE="$(mktemp)"
trap 'rm -f "$APT_SOURCE"' EXIT

if [[ ! -f "$PACKAGE_LIST" ]]; then
  echo "ERROR: Package list not found: $PACKAGE_LIST" >&2
  exit 1
fi

# Debian Bookworm firmware packages are in non-free-firmware.
cat > "$APT_SOURCE" <<'EOF'
deb http://deb.debian.org/debian bookworm main contrib non-free non-free-firmware
EOF

# Use a temporary APT source file so we do not collide with the repo
# already configured in /etc/apt/sources.list.
apt-get \
  -o Dir::Etc::sourcelist="$APT_SOURCE" \
  -o Dir::Etc::sourceparts=/dev/null \
  update -o Acquire::Retries=3

bad=0
while IFS= read -r package || [[ -n "$package" ]]; do
  # Trim surrounding whitespace.
  package="${package#"${package%%[![:space:]]*}"}"
  package="${package%"${package##*[![:space:]]}"}"

  case "$package" in
    ""|\#*) continue ;;
  esac

  if ! apt-cache \
      -o Dir::Etc::sourcelist="$APT_SOURCE" \
      -o Dir::Etc::sourceparts=/dev/null \
      show "$package" >/dev/null 2>&1; then
    echo "MISSING: $package"
    apt-cache \
      -o Dir::Etc::sourcelist="$APT_SOURCE" \
      -o Dir::Etc::sourceparts=/dev/null \
      policy "$package" || true
    bad=1
  fi
done < "$PACKAGE_LIST"

if (( bad )); then
  echo "ERROR: One or more package names were not found in the configured repositories." >&2
  exit 1
fi

echo "All packages found."
