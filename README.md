# Hybridus UI 0.7 source kit

GPL-3.0 source kit for the experimental Hybridus UI 0.7 changes on Unleashed 095E / Flipper Zero F7. This repository publishes source evidence and reproducible checks, not a firmware binary or release.

## Scope

- Quick Settings one-page navigation: brightness and volume sliders; Bluetooth, Dummy Mode, vibration, sound-only Mute and left/right orientation controls; directional focus, OK activation and single-Back exit.
- Main-menu category discovery/grouping while preserving the existing Apps entry and existing FAP/JS resources; case-insensitive ordering and Tools/Clock handling.
- Animated 14x14 monochrome icons for Bluetooth, Games, Media and Scripts.
- UI spacing/visibility corrections: readable JS icon on a dark file silhouette, separated slider borders and two white divider columns.
- Mute persistence: avoid an identical private `.hybridus-mute` rewrite after validating the existing file; failed or changed reads still save immediately.
- A narrow preserve-updater guard for the experimental package, statically checked in the source kit.

The patch also includes a small getter helper and the required source/resource changes. The exact patch is in `hybridus-ui-0.7-095e-preserve.patch`; `build.sh` clones the pinned upstream tag and builds without flashing a device.

## Provenance and limits

Base: DarkFlippers/unleashed-firmware tag `unlshd-095`, commit `9c6327764c18fc8376b5941aa8bde79fe681fe8f`, GPL-3.0. The visual slider reference is documented in NOTICE. This is not an official Unleashed release and is not yet an upstream PR. The kit targets API 88.26; it is not a source reconstruction of the separately installed API 88.27 LTO package.

Host tests, patch application, package/CRC checks and static verification are included. No physical Flipper, qFlipper update, USB/BLE host, endurance or radio test is claimed. Previews are software renders, not device photos.

## Flash evidence

The controlled UI 0.7 build is reported as 879,196 bytes, 215 pages, and +48 bytes versus the 0.6.2 baseline; the report explains that this is the total patch cost, not a per-feature delta. The Mute change reduces repeated private-file requests on the microSD path; it does not prove reduced MCU flash wear. LTO and radio-boundary caveats are documented in the reports.

Separate workstreams are intentionally not included: DUCKY_LANG/BadUSB, BLE custom name, VGM FAP/UF2 and RGB event/sync. Their statuses and blockers are not silently merged into this UI kit.
