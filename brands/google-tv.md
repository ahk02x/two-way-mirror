# Sony, Philips, TCL, Hisense and others running Google TV / Android TV

These sets have **two** layers of collection: Google's, and often a **third-party ACR vendor the
manufacturer added on top** — most commonly **Samba TV**. You have to turn off both. People
routinely do the Google half and think they are done.

## 1. Google's layer

- `Settings` → `Privacy` → `Usage & Diagnostics` → Off
- `Settings` → `Privacy` → `Ads` → **Opt out of Ads Personalization** → On, then **Reset
  advertising ID**
- `Settings` → `Privacy` → `Location` → Off (or "Use Wi-Fi to estimate location" → Off)
- `Settings` → `Privacy` → `Google Assistant` → review **Speech Services**; turn off saved audio
- `Settings` → `System` → `About` → check for a manufacturer telemetry item

## 2. The manufacturer's layer — this is the one people miss

Look in `Settings` → `Privacy`, `Settings` → `System`, or a manufacturer-branded menu, for:

- **Samba TV**, **Samba Interactive TV**, or **Interactive TV** → Off. Sony has shipped this on many
  models. Its consent screen historically appeared during setup with an "Interactive TV" label that
  did not mention viewing data on the visible screen.
- **Sony:** `Settings` → `System` → `About` → `Legal information` / `Privacy setting` — review each
  toggle. Sony has also used **Samba** and its own **Sony Data Collection**.
- **TCL / Hisense on Google TV:** look for a vendor privacy menu separate from Google's.
- **Philips:** look for **Ambilight+hue** and vendor analytics separately.

## 3. Check what is actually installed

`Settings` → `Apps` → `See all apps` → `Show system apps`. Look for anything named *Samba*,
*Alphonso*, *Inscape*, *ACR*, or a vendor analytics package. If present, open it and use **Disable**
(you usually cannot uninstall system apps, but disabling stops it).

## Known behaviour

- Blocking Google domains wholesale at the network will break Google TV badly — the launcher, the
  Play Store, and app auth all depend on them. Block the specific ad and analytics hostnames in
  [../network/dns-blocklist.txt](../network/dns-blocklist.txt), not `google.com`.
- Samba TV's opt-in has historically been accepted by the large majority of users because of how the
  setup screen is worded. If you have never explicitly turned it off, assume it is on.
