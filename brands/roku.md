# Roku (players, and TCL / Hisense / Sharp / Philips TVs running Roku TV)

**The setting you are looking for is called "Smart TV Experience"** (on Roku TVs) or lives under
`Privacy` (on Roku players).

## Turn off ACR

- `Settings` → `Privacy` → **Smart TV Experience** → uncheck **Use info from TV inputs**

That checkbox is ACR on HDMI and antenna inputs. Unchecking it is the main step.

## Also turn off

- `Settings` → `Privacy` → **Advertising** → check **Limit ad tracking**
- `Settings` → `Privacy` → **Microphone** → set channel microphone access to **Never**
- `Settings` → `Privacy` → **Voice** → review and disable saved voice recordings
- `Settings` → `System` → `Advanced system settings` → **Device connect** — turn off if unused

## Reset the advertising ID

There is no explicit reset on most Roku firmware. A factory reset generates a new one, which is a
heavy option. Enabling **Limit ad tracking** is the practical measure.

## Known behaviour

- Roku's telemetry is unusually chatty. Expect ongoing connections to `*.logs.roku.com` even after
  opting out — these carry operational and usage data distinct from ACR. Blocking them at the
  network is effective and does not break playback in most reports, but see the caveat in
  [../network/dns-blocklist.txt](../network/dns-blocklist.txt).
- Roku's home screen ads are core to the product and cannot be removed in settings.
- Measurement research (ACM CCS 2019, see [../evidence/](../evidence/)) found third-party trackers
  embedded in a large fraction of Roku channels, independent of Roku's own collection. Turning off
  ACR does not touch what individual channels do.
