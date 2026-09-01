# Amazon Fire TV (sticks, cubes, and Fire TV Edition televisions)

Amazon does not run screen-fingerprinting ACR in the way VIZIO or Samsung do, but it collects
detailed app and device usage data and ties it to your Amazon account — which is, for most people,
a richer identifier than an IP address.

## Turn off data collection

`Settings` → `Preferences` → `Privacy Settings`:

- **Device Usage Data** → Off
- **Collect App Usage Data** → Off
- **Interest-based Ads** → Off

`Settings` → `Preferences` → `Data Monitoring` → Off (this one is a bandwidth feature, but it
reports)

## Also turn off

- `Settings` → `Preferences` → `Featured Content` → **Allow Video Autoplay** → Off and **Allow Audio
  Autoplay** → Off. Not privacy exactly, but it stops the home screen streaming ads at you.
- `Settings` → `Alexa` / `Preferences` → review voice recordings; delete history and set
  auto-delete at [amazon.com/alexaprivacy](https://www.amazon.com/alexaprivacy)
- On the Amazon website, not the TV: `Account` → `Advertising Preferences` → opt out. This is
  account-level and affects more than the TV.

## Known behaviour

- `device-metrics-us.amazon.com` is the primary telemetry endpoint and is widely blocked at the
  network with no loss of function. It is in [../network/dns-blocklist.txt](../network/dns-blocklist.txt).
- Fire TV sideloading and developer options do not affect telemetry either way.
- Because collection is tied to your Amazon account rather than the device, a factory reset does not
  reset your profile. The account-level opt-out matters more here than on other platforms.
