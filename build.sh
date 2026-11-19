#!/bin/sh
# Rebuild only. Never flashes, erases or accesses a device.
set -eu
here=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
base=9c6327764c18fc8376b5941aa8bde79fe681fe8f
suffix=hybridus-ui-0.7-095e-preserve
[ ! -e "$here/source" ] || { echo 'source already exists: use a fresh copy' >&2; exit 1; }
git clone --branch unlshd-095 --depth 1 https://github.com/DarkFlippers/unleashed-firmware.git "$here/source"
cd "$here/source"
[ "$(git rev-parse HEAD)" = "$base" ]
git submodule update --init --recursive
git apply --check "$here/hybridus-ui-0.7-095e-preserve.patch"
git apply "$here/hybridus-ui-0.7-095e-preserve.patch"
# 095E has the same firmware source tag; its Extra Apps remain on the user's SD.
export DIST_SUFFIX="$suffix" WORKFLOW_BRANCH_OR_TAG="$suffix"
./fbt -j2 updater_minpackage DEBUG=0 COMPACT=1 DIST_SUFFIX="$suffix"
python3 "$here/package-min.py" "$PWD"
