# Why your DNS blocklist is probably not working on the TV

You set up Pi-hole. You added the list. The TV still phones home. Here is why, in order of how often
it is the cause.

## 1. The TV ignores the DNS server you gave it

This is the big one, and it is common enough on Samsung sets specifically that it should be your
first assumption. The TV takes your DHCP-assigned DNS server, and then queries a hardcoded public
resolver anyway — typically `8.8.8.8`.

**Fix — force all DNS through your resolver.** On your router, add a NAT rule that redirects any
outbound traffic to port 53 back to your own DNS server, and a firewall rule that blocks port 53 to
anywhere else.

On OPNsense or pfSense, this is a port-forward on the LAN interface:

```
Interface:        LAN
Protocol:         TCP/UDP
Source:           LAN net
Destination:      ! (invert) LAN address
Destination port: 53 (DNS)
Redirect target:  127.0.0.1  (or your Pi-hole address)
Redirect port:    53
```

Then verify: the TV's queries should now appear in your resolver's log. If they do not, it is not
using DNS at all — see #3.

## 2. The TV uses encrypted DNS (DoH / DoT)

DNS-over-HTTPS looks like ordinary HTTPS traffic on port 443, so your resolver never sees it and
your blocklist never applies.

**Fix:**
- Block **port 853** outbound (DNS-over-TLS) at the firewall. Cheap and effective.
- Block the known DoH endpoint hostnames and IP ranges (`dns.google`, `cloudflare-dns.com`,
  `mozilla.cloudflare-dns.com`, `dns.quad9.net`, and others). Maintained lists exist; search for
  "DoH blocklist."
- The complete fix is #4 below.

## 3. The TV connects to hardcoded IP addresses

No DNS lookup happens at all, so nothing to block. Less common, but it happens, and it defeats
every DNS-based approach permanently.

**Fix:** #4 below. There is no DNS-layer answer to this.

## 4. The actual fix: stop treating this as a DNS problem

DNS filtering is a *request* that the device look somewhere else. A firewall rule is not a request.

**Give the TV a static IP (DHCP reservation), then write firewall rules:**

- **Allow** TV → your DNS server, port 53
- **Allow** TV → your LAN, if you use local casting or DLNA
- **Allow** TV → the specific services you actually want (or nothing at all)
- **Block** TV → WAN, everything else, and log it

Now the TV can be as chatty as it likes. Nothing leaves.

If you want the TV's own apps to keep working, you cannot do a blanket WAN block — you are back to
allowing the app CDNs and blocking the telemetry, which is a maintenance treadmill. This is the real
argument for the four-minute version in the main README: **use an external streaming box and let the
TV be a screen.** It converts an ongoing arms race into a one-time firewall rule.

## 5. Verify, do not assume

Blocking without verifying is how people end up confidently wrong.

- Watch your resolver's query log with the TV as the only thing on
- Watch the firewall's block counters — a rule with zero hits is either working perfectly or not
  matching at all, and you cannot tell which without looking
- If your router exports flow data (NetFlow, sFlow), look at the TV's actual destinations rather
  than at what you expect them to be

A blocklist you have not verified is a comfort object.
