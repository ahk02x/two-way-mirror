# The durable fix: firewall rules and VLAN isolation

Settings can be reset by a firmware update. Blocklists can be routed around. A firewall rule holds
until you change it.

## Level 1 — pin the TV and block its internet (any router with firewall rules)

1. **Give the TV a fixed address.** DHCP reservation on its MAC, so rules keep matching.
2. **Block it from the WAN.** One rule: source = TV address, destination = WAN / "any", action =
   block, logging = on.
3. **Allow what you need back.** Usually just your DNS server and your LAN, if you cast to it.

The TV loses its apps. That is the point — you replace them with a device you chose.

Test it: the TV should fail to reach the internet, and local casting from your phone should still
work.

## Level 2 — VLAN isolation (OPNsense, pfSense, UniFi, OpenWrt, MikroTik)

Better, because it covers every current and future device of this class without per-device rules.

1. Create an **IoT VLAN** — a separate network for TVs, speakers, plugs, cameras, appliances.
2. Put the TV on it, along with everything else that has a cloud service and a firmware update
   channel.
3. Rules on that VLAN:
   - **Allow** IoT → your DNS server
   - **Allow** IoT → NTP, if devices need time sync
   - **Block** IoT → all other local networks (this is the part that matters — it stops a
     compromised TV from reaching your laptop, NAS, or backups)
   - **Block** IoT → WAN, or allow only a specific short list
4. If you want to cast from your phone on the main network to a TV on the IoT VLAN, you need
   **mDNS reflection / Avahi** between the two VLANs, plus a narrow allow rule for the casting
   protocol. Most routers that support VLANs support this.

The second rule — IoT cannot reach your real network — is worth more than the ACR blocking. A TV is
an internet-connected computer running an old Android or Linux kernel that the vendor stops patching
years before you stop watching it. Treat it as hostile hardware you happen to own.

## Level 3 — no network at all

Do not give the TV Wi-Fi credentials. Do not plug in the ethernet.

Some sets nag, some hide settings behind a network check, and a few refuse to complete initial setup
without a connection. Workaround: connect it once to complete setup, opt out of everything, then
remove the credentials (`Settings` → `Network` → forget) or block it at the router as above.

This is the only approach with no ongoing maintenance.

## A note on what you are defending against

Two separate things, worth keeping distinct:

- **Surveillance** — the vendor monetising your viewing. Handled by opt-outs plus egress blocking.
- **Exposure** — an unpatched consumer device with a network stack sitting on the same network as
  everything you own. Handled only by segmentation.

The second one is the one people underrate, and it is the one that turns a privacy annoyance into an
actual security incident. If you do one thing from this file, do the VLAN.
