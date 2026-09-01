# Network-level blocking

Device settings depend on the vendor honouring them. Network blocking does not.

Do both. Settings first, because they are free and they stop collection at the source. Network
blocking second, as the backstop for the collection that continues anyway — and there is always
some.

| File | What it is |
|---|---|
| [dns-blocklist.txt](dns-blocklist.txt) | Hostnames, tiered by how safe they are to block |
| [dns-is-not-enough.md](dns-is-not-enough.md) | **Read this.** Why your blocklist is probably not working on the TV |
| [router-firewall.md](router-firewall.md) | The durable fix — firewall rules and VLAN isolation |
| [pihole-nextdns.md](pihole-nextdns.md) | Applying the list in Pi-hole, AdGuard Home, or NextDNS |

## The honest ranking of approaches

1. **TV never touches the network.** Total, free, no maintenance. Costs you the built-in apps.
2. **TV on an isolated VLAN with no WAN access**, apps come from a device you control. Nearly as
   good, keeps local casting working, requires a real router.
3. **Firewall rule: TV may not reach the internet, only your DNS/local services.** Good, simpler.
4. **Forced DNS + blocklist.** Effective against most, defeated by hardcoded IPs and DoH.
5. **Blocklist on your normal DNS.** The weakest, and the one almost everyone stops at. TVs are the
   single worst offenders for ignoring router-assigned DNS.

Most guides give you #5 and let you believe you got #1.
