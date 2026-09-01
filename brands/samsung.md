# Samsung (Tizen)

**The setting you are looking for is called "Viewing Information Services."** That is Samsung's name
for ACR. Turning it off is the single most important step on a Samsung TV.

## Turn off ACR

Menu paths differ by year and region. The setting name is stable — navigate until you find it.

- **2021 and newer:** `Settings` → `All Settings` → `General & Privacy` → `Terms & Privacy`
  (sometimes `Privacy Choices`) → uncheck **Viewing Information Services**
- **2018–2020:** `Settings` → `Support` → `Terms & Policy` → uncheck **Viewing Information Services**
- **Older:** `Menu` → `Smart Hub` → `Terms & Policy` → **SyncPlus and Marketing** / **Viewing
  Information Services**

You may be asked to confirm with a warning about losing recommendations. Confirm. The
"recommendations" are advertising.

## Also turn off

Same `Terms & Privacy` screen, or nearby:

- **Interest-Based Advertising** (sometimes **Interest-Based Advertisements Service**) — off
- **Voice Recognition Services** — off, unless you use voice control
- **Additional Data Collection / Device Data** — off
- **SyncPlus and Marketing** — off

## Reset the advertising ID

`Settings` → `General & Privacy` → `Terms & Privacy` → **Reset Device Advertising ID** (older sets
call it **Reset Ad ID**). Do this after opting out, so the profile already built against the old ID
is orphaned. Repeat occasionally.

## Ambient/Art mode

If you use Ambient Mode or a Frame TV, note that it fetches content and reports engagement. It is
not ACR, but it is a network dependency you may not want.

## Known behaviour

- **Samsung TVs frequently ignore the DNS server your router hands out** and query hardcoded public
  resolvers instead. DNS blocklists alone will not reliably stop a Samsung. See
  [../network/dns-is-not-enough.md](../network/dns-is-not-enough.md) for the fix (redirect or block
  outbound DNS at the router).
- **Firmware updates re-prompt.** After a major update the TV often shows the terms screen again,
  and the default is accept. Re-check after every update.
- Some regions ship with ACR consent bundled into the mandatory privacy policy acceptance. If you
  cannot decline it separately, network blocking is your only remaining option.

## Verify

After opting out, check [../network/dns-blocklist.txt](../network/dns-blocklist.txt) for the Samsung
telemetry hostnames and watch your resolver logs. Continued queries to `samsungacr.com` after
opt-out is a finding worth [reporting in an issue](../CONTRIBUTING.md).
